import argparse
import ast
import csv
import datetime
import gc
import hashlib
import io
import itertools
import json
import logging
import math
import os
import re
import socket
import sys
import threading
import time
import traceback
import uuid
from getpass import getpass
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from io import BytesIO
from multiprocessing import Pool, Manager
from time import sleep

import cv2
import imageio.v3 as iio
import numpy as np
import pydicom
import requests
from imageio import RETURN_BYTES
from pathy import Pathy
from pydicom import uid
from pydicom._uid_dict import UID_dictionary
from pydicom.encaps import decode_data_sequence
from pydicom.encaps import encapsulate, generate_pixel_data_frame
from pydicom.errors import InvalidDicomError
from pydicom.filewriter import write_file_meta_info
from pydicom.pixel_data_handlers import apply_color_lut
from pynetdicom import AE, evt, ALL_TRANSFER_SYNTAXES, sop_class
from tqdm import tqdm
from watchdog.events import FileCreatedEvent, FileMovedEvent, FileModifiedEvent, DirCreatedEvent
from watchdog.events import FileSystemEventHandler
from watchdog.observers.polling import PollingObserver

from echoloader.config import DEFAULT_PORT, DEFAULT_TLS_PORT, get_env_var
from echoloader.dimse import DEFAULT_AE_TITLE, detail_to_store
from echoloader.dimse.tls import server_context, tls_certs
from echoloader.login import Us2Cognito, unpack
from echoloader.sync import Sync

logger = logging.getLogger('echolog')
for sop_class_uid in ['1.2.840.10008.5.1.4.1.1.3', '1.2.840.10008.5.1.4.1.1.6']:
    sop_class._STORAGE_CLASSES[UID_dictionary[sop_class_uid][-1]] = sop_class_uid


class ConfigUpdatedException(Exception):
    pass


def setup_logging(filename=None, verbose=None):
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG if verbose else logging.WARNING)
    logging.getLogger().handlers[0].setFormatter(logging.Formatter(
        "[%(asctime)s][%(processName)10s][%(pathname)s:%(lineno)d]\n%(message)s"))
    if filename:
        fh = logging.FileHandler(filename)
        logging.getLogger().addHandler(fh)


class ENV:
    def __init__(self, env):
        prefix = f'{env}-'.replace('production-', '')
        self.cloud = '://' not in env
        self.api_url = f"https://{prefix}api.us2.ai" if self.cloud else env


def is_video(img=None, shape=None):
    shape = shape or (isinstance(img, np.ndarray) and img.shape)
    return shape and (len(shape) == 4 or (len(shape) == 3 and shape[-1] > 4))


def ybr_to_rgb(img):
    return cv2.cvtColor(img, cv2.COLOR_YCR_CB2BGR)


def blank_top_bar(media, regions):
    video = is_video(media)
    image = np.mean(media, axis=0) if video else media
    new_image = np.mean(image[..., :3], axis=-1) if 3 <= image.shape[-1] <= 4 else image
    binary_image = (new_image > 2).astype('uint8')
    h = int(binary_image.shape[0] * 0.2)
    sum_pixel = np.sum(binary_image[:h, :], axis=1)
    top_bar = np.where(sum_pixel > (binary_image.shape[0] * 0.88))
    top_bar_bottom = 0
    if len(top_bar[0]) != 0:
        new_image[top_bar, :] = 0
        image[top_bar, :] = 0
        top_bar_bottom = top_bar[0][-1] + 1
    top_bar_bottom = max(top_bar_bottom, 40)
    mask = np.ones_like(media[0] if video else media)
    mask[:top_bar_bottom] = 0
    for region in regions:
        xo, xn = region.RegionLocationMinX0, region.RegionLocationMaxX1
        yo, yn = region.RegionLocationMinY0, region.RegionLocationMaxY1
        mask[yo:yn, xo:xn] = 1
    media *= mask
    return media


def mpeg4hp41(ds):
    return iio.imread(next(generate_pixel_data_frame(ds.PixelData)))


def unusual_frame_mean(px: np.ndarray, threshold=100):
    """
    If mean pixel value of frame is larger than threshold, background is likely non-black
    (usually happens when dicom tag is RGB but the frames are actually in YBR).
    """
    frame = px[px.shape[0] // 2] if is_video(px) else px  # take middle frame for video
    return cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)[..., -1].mean() > threshold


def media_iter(dicom):
    try:
        seq = decode_data_sequence(dicom.PixelData)
        if not seq:
            raise ValueError('No data sequence found')
        for b in seq:
            yield iio.imread(io.BytesIO(b))
    except Exception as exc:
        logger.info(f'Failed to decode JPEG compressed frame bytes due to {exc}, falling back to pixel_array')
        handler = parse_dicom_pixel.custom_handlers.get(dicom.file_meta.TransferSyntaxUID)
        px = handler(dicom) if handler else dicom.pixel_array
        if isinstance(px, np.ndarray) and not is_video(px):
            px = [px]
        yield from px


def parse_dicom_pixel(dicom, anonymize=True):
    """Parse color space and coerce to RGB, and anonymize by blanking out top bar."""
    px = media_iter(dicom)
    pi = dicom.PhotometricInterpretation
    px = (ybr_to_rgb(img) if pi in ['YBR_FULL', 'YBR_FULL_422', 'RGB'] and unusual_frame_mean(img) else img
          for img in px)
    px = ((apply_color_lut(img, dicom) // 255).astype('uint8') if pi in ['PALETTE COLOR'] else img for img in px)
    px = (np.repeat(np.expand_dims(img, -1), 3, -1) if len(img.shape) < 3 else img for img in px)
    if anonymize:
        px = (blank_top_bar(img, getattr(dicom, "SequenceOfUltrasoundRegions", [])) for img in px)
    sample = next(px)
    px = itertools.chain([sample], px)
    shape = (getattr(dicom, 'NumberOfFrames', 1), *sample.shape)
    return px, shape


parse_dicom_pixel.custom_handlers = {
    uid.MPEG4HP41: mpeg4hp41,
}


def ensure_even(stream):
    # Very important for some viewers
    if len(stream) % 2:
        return stream + b"\x00"
    return stream


def person_data_callback(ds, e):
    if e.VR == "PN" or e.tag == (0x0010, 0x0030):
        del ds[e.tag]


def pad_to_multiple(arr, size, dims=(1, 2)):
    pad_dims = [(0, size - (s % size)) if i in dims else (0, 0) for i, s in enumerate(arr.shape)]
    return np.pad(arr, pad_dims, 'constant')


def encode_video(out, stream, fps, bit_rate=512000 * 5):
    with iio.imopen(out, "w", plugin="pyav", extension='.mp4') as out_file:
        out_file.init_video_stream('libx264', fps=fps)
        out_file._video_stream.codec_context.bit_rate = bit_rate
        for frame in stream:
            out_file.write_frame(frame)


def package_dicom(ds, anonymize, compress):
    # Populate required values for file meta information
    ds.remove_private_tags()
    if anonymize:
        ds.walk(person_data_callback)
    if not anonymize and not compress:
        return
    if not hasattr(ds, 'PixelData'):
        return
    media, shape = parse_dicom_pixel(ds, anonymize)
    ds.is_little_endian = True
    ds.is_implicit_VR = False

    ds.BitsStored = 8
    ds.BitsAllocated = 8
    ds.HighBit = 7
    ds.Rows, ds.Columns, ds.SamplesPerPixel = shape[1:]
    ds.PhotometricInterpretation = "YBR_FULL_422"
    if shape[0] > 1:
        ds.StartTrim = 1
        ds.StopTrim = ds.NumberOfFrames = shape[0]
        fps = getattr(ds, 'CineRate', int(1000 / getattr(ds, 'FrameTime', 40)))
        ds.CineRate = ds.RecommendedDisplayFrameRate = fps
        ds.FrameTime = round(1000 / ds.CineRate, 4)
        ds.ActualFrameDuration = math.ceil(1000 / ds.CineRate)
        ds.PreferredPlaybackSequencing = 0
        ds.FrameDelay = 0
        if compress:
            ds.file_meta.TransferSyntaxUID = uid.MPEG4HP41
            bs = io.BytesIO()
            encode_video(bs, (pad_to_multiple(img, 16, (0, 1)) for img in media), fps=fps)
            ds.PixelData = encapsulate([bs.getvalue()])
        else:
            ds.file_meta.TransferSyntaxUID = uid.JPEGBaseline8Bit
            ds.PixelData = encapsulate([iio.imwrite(RETURN_BYTES, img, extension='.jpg') for img in media])
    else:
        ds.file_meta.TransferSyntaxUID = uid.JPEGBaseline8Bit
        ds.PixelData = encapsulate([iio.imwrite(RETURN_BYTES, next(media), extension='.jpg')])
    ds['PixelData'].is_undefined_length = True


def size(path):
    stat = path.stat()
    return getattr(stat, 'size', getattr(stat, 'st_size', None))


def wait_file(path):
    path = Pathy.fluid(path)
    old = None
    cur = size(path)
    while old != cur or not cur:
        sleep(1)
        old, cur = cur, size(path)


def create_proxy(args):
    class Proxy(SimpleHTTPRequestHandler):
        def do_request(self, method):
            url = f'{args.auth.api_url}{self.path}'
            headers = dict(self.headers)
            headers.update(args.auth.get_headers())
            headers['Host'] = 'proxy.us2.ai'
            data = self.rfile.read(int(self.headers['Content-Length'] or 0))
            response = getattr(requests, method)(url, headers=headers, stream=True, data=data)
            self.send_response(response.status_code)
            for k, v in response.headers.items():
                self.send_header(k, v)
            self.end_headers()
            self.copyfile(response.raw, self.wfile)

        def do_GET(self):
            self.do_request('get')

        def do_PUT(self):
            self.do_request('put')

        def do_POST(self):
            self.do_request('post')

        def do_DELETE(self):
            self.do_request('delete')

        def do_OPTIONS(self):
            self.do_request('options')

    return Proxy


def initializer(filename, verbose):
    setup_logging(filename, verbose)


class Handler(FileSystemEventHandler):
    def __init__(self, args):
        self.args = args
        self.child_observer = None
        self.watching = None
        self.pool = Pool(args.n, initializer=initializer, initargs=(args.log, args.verbose))
        self.pbar = tqdm(total=0)
        if self.args.csv_out:
            with open(self.args.csv_out, 'a', newline='') as f:
                csv.writer(f).writerow(self.args.extracted_details)

    def __getstate__(self):
        self_dict = self.__dict__.copy()
        del self_dict['pool']
        del self_dict['pbar']
        return self_dict

    def __setstate__(self, state):
        self.__dict__.update(state)

    def processing(self):
        return self.pbar.n < self.pbar.total or self.child_observer

    def stop(self):
        self.pool.terminate()
        if self.child_observer:
            self.child_observer.stop()

    def join(self):
        self.pool.join()
        if self.child_observer:
            self.child_observer.join()

    def handle_existing_files(self, src):
        paths = [src] if src.is_file() else [p for p in src.rglob(self.args.src_glob) if p.is_file()]
        details = self.args.src_details and re.compile(self.args.src_details)
        for i, path in enumerate(paths):
            kwargs = {}
            if details:
                match = details.search(path.as_posix())
                if match:
                    kwargs = match.groupdict()
                    s = f"Matched path details: {kwargs} on {path.as_posix()}"
                    logger.info(s)
                else:
                    s = f"No match for path details regex on {path.as_posix()}"
                    logger.warning(s)
                if i == 0 and not self.args.y and input(f'{s}, Continue (y/n): ') != 'y':
                    return False
            self.handle(path, **kwargs)
        return True

    def watch(self, src):
        logger.warning(f"watching files recursively in {os.path.abspath(src)}")
        if not self.child_observer:
            self.child_observer = PollingObserver()
            self.child_observer.start()
        if self.watching:
            self.child_observer.remove_handler_for_watch(self, self.watching)
        self.watching = self.child_observer.schedule(self, src, recursive=True)
        self.handle_existing_files(src)

    def handle_err(self, err):
        if isinstance(err, InvalidDicomError):
            self.pbar.total -= 1
            self.pbar.update(0)
            return
        self.pbar.update(1)

    def handle(self, *vargs, **kwargs):
        self.pbar.total += 1
        self.pbar.refresh()
        self.pbar.disable = False
        self.pool.map_async(HandlerWorker.work, [(self.args, vargs, kwargs)],
                            error_callback=lambda err: self.handle_err(err),
                            callback=lambda _: self.pbar.update(1))

    def on_any_event(self, event):
        logger.debug(f'got event {event}')
        if isinstance(event, (FileCreatedEvent, FileMovedEvent, FileModifiedEvent)):
            path = event.src_path
            wait_file(path)
            self.handle(path)


class DirHandler(FileSystemEventHandler):
    def __init__(self, handler: Handler):
        self.handler = handler

    def on_any_event(self, event):
        logger.debug(f'got event {event}')
        if isinstance(event, DirCreatedEvent):
            self.handle_dir(event)

    def handle_dir(self, event):
        src = event.src_path
        logger.info(f'Processing child dir {src}')
        src = src and Pathy.fluid(src)
        self.handler.watch(src)


def validattr(obj, e):
    return hasattr(obj, e) and bool(getattr(obj, e))


def prune_invalid_tags(ds, groups=(0x200d,)):
    for k in list(ds._dict.keys()):
        if k.group in groups:
            logger.info(f'Pruned {k} from dataset')
            ds._dict.pop(k)


def anonymize_settings(user, default):
    res = [*default]
    if echoloader_settings := user.get('echoloader_settings', {}):
        res[0] = echoloader_settings.get('anonymize', res[0])
        if res[0]:
            res[1] = [f'{f}:{v}' for f, v in echoloader_settings.get('anonymize_settings', {}).items()] or res[1]
    return res


class HandlerWorker:
    def __init__(self, args, path=None, ds=None, called_ae_title=None, calling_ae_title=None, f=None, **kwargs):
        self.path = path
        self.kwargs = kwargs
        self.ds = ds
        self.called_ae_title = called_ae_title
        self.calling_ae_title = calling_ae_title
        self.auth = getattr(args, 'auth', None)
        self.api_url = getattr(self.auth, 'api_url', None)
        self.params = {'v': args.v}
        self.f = f
        self.params_trial = args.params_trial
        self.params_pid = args.params_pid
        self.params_visit = args.params_visit
        self.anonymize = args.anonymize
        self.pseudonymize = args.pseudonymize
        self.args = args

    @staticmethod
    def work(t):
        args, vargs, kwargs = t
        HandlerWorker(args, *vargs, **kwargs).process()

    def user(self, ae_title):
        user_details = requests.get(f'{self.api_url}/users/users_by_ae/{ae_title}', params=self.params,
                                    headers=self.auth.get_headers())

        if user_details.status_code != 200:
            raise ValueError(f'Error getting user details for {ae_title}')

        user_details = unpack(user_details)
        pacs_enabled = user_details and user_details.get('pacs_config') and user_details.get('pacs_config').get(
            'enabled')
        if not pacs_enabled:
            raise ValueError(f'Cloud PACS is not enabled for {ae_title}')
        return user_details

    def file_params(self, ds, ae_title, user=None, filename=None):
        customer = getattr(self.args, 'customer', '') or ae_title
        stem = '_'.join(map(str, filter(bool, [ds.SOPInstanceUID, filename])))
        kwargs = self.kwargs
        params = {
            'customer': str(customer or ''),
            'ae_title': str(ae_title or ''),
            'trial': str(kwargs.get('trial')
                         or next((getattr(ds, e) for e in self.params_trial if validattr(ds, e)),
                                 getattr(self.args, 'trial', None) or customer or '')),
            'patient_id': str(kwargs.get('patient_id')
                              or next((getattr(ds, e) for e in self.params_pid if validattr(ds, e)), 'NA')),
            'visit_id': str(kwargs.get('visit_id')
                            or next((getattr(ds, e) for e in self.params_visit if validattr(ds, e)), 'No Study ID')),
            'filename': str(kwargs.get('filename') or f"{stem}.dcm"),
        }
        if self.args.trial_id:
            params['trial_id'] = self.args.trial_id
        if user:
            params['customer'] = user.get('customer')
            pacs_config = user.get('pacs_config')

            customer = None
            groups = user.get('permissions', [])
            s3 = [g for g in groups if g.startswith('s3-')]
            if s3:
                customer = s3[0].split('-', 1)[1]
            elif 'upload' in groups or 'admin' in groups:
                customer = user.get('cognito_id')

            if not customer:
                raise ValueError(f'No customer found for {ae_title}, cloud sync was enabled')

            params['trial'] = user.get('email', customer)
            params['customer'] = customer

            if pacs_config.get('enable_cloud_sync'):
                logger.info(f'Cloud sync was enabled for AET: {ae_title}, customer: {customer}')
                params['enable_cloud_sync'] = True
            if trial_id := user.get('echoloader_settings', {}).get('trial_id'):
                params['trial_id'] = trial_id
        return params

    def upload(self, ds, param):
        logger.info(f'uploading {param}')
        content_type = 'application/dicom'
        auth = self.args.auth
        env = self.args.env
        headers = auth.get_headers()
        param['content_type'] = content_type
        upload_param = {}
        url = f"{auth.api_url}/dicom/upload"
        if env.cloud:
            r = requests.get(url, params=param, headers=headers)
            d = unpack(r)
            url = d['url']
            headers = d['headers']
        else:
            upload_param = param
        buf = BytesIO()
        ds.save_as(buf, write_like_original=False)
        buf.seek(0)

        for retry_attempt in range(self.args.upload_retries):
            try:
                upload_response = requests.put(url, data=buf.read(), headers=headers, params=upload_param)
                upload_response.raise_for_status()

                logger.debug(f'Response code: {upload_response.status_code}, Attempt: {retry_attempt + 1}')
                return upload_response
            except requests.exceptions.RequestException as exc:
                code = exc.response.status_code if exc.response else None
                logger.error(f'Error uploading {url} due to {exc}, Response code: {code}, Retry.. {retry_attempt + 1}')

                if retry_attempt == self.args.upload_retries - 1:
                    logger.error(f'Retries completed. Error uploading {url} due to {exc}')
                    raise exc

                time.sleep(self.args.upload_retry_interval)
                self.auth.refresh()
                continue

    def pseudonymization(self, ds):
        for tag in self.pseudonymize:
            action = 'pseudonymize'
            if ':' in tag:
                tag, action = tag.split(':')
            old = getattr(ds, tag, None)
            if not old:
                continue
            if action in ['remove']:
                new = None
            elif action in ['pseudonymize', 'anonymize']:
                new = hashlib.sha256(old.encode()).hexdigest()[:8]
            elif action in ['keep']:
                new = old
            else:
                raise ValueError(f'Invalid action {action}')
            logger.info(f'{action} {tag} from {getattr(ds, tag)} to {new}')
            if self.args.pseudonymize_file:
                with Pathy.fluid(self.args.pseudonymize_file).open('a+') as f:
                    f.seek(0)
                    entry = f"{tag},{old},{new}"
                    if entry not in {t.strip() for t in f}:
                        f.write(f"{entry}\n")
            setattr(ds, tag, new)

    def process(self):
        try:
            user = None
            ae_titles = [aet for aet in [self.calling_ae_title, self.called_ae_title] if aet]
            ae_title = next(iter(ae_titles), None)
            if self.args.enforce_ae_title and ae_titles:
                excs = []
                for aet in ae_titles:
                    try:
                        user = self.user(aet)
                        ae_title = aet
                        break
                    except ValueError as exc:
                        excs.append(exc)
                else:
                    raise ExceptionGroup(f'{", ".join(map(str, excs))} - skipping!', excs)
                self.anonymize, self.pseudonymize = anonymize_settings(user, (self.anonymize, self.pseudonymize))
            path = self.path and Pathy.fluid(self.path)
            self.f = self.f or path.open('rb')
            ds = self.ds or pydicom.dcmread(self.f, force=True)
            prune_invalid_tags(ds)
            if self.pseudonymize:
                self.pseudonymization(ds)
            params = self.file_params(ds, ae_title=ae_title, user=user, filename=getattr(path, 'stem', None))
            logger.info(f'processing {params}')
            extracted = self.args.extracted
            key = tuple(getattr(ds, e, None) for e in self.args.extracted_details)
            if key not in extracted:
                for f in self.args.filter:
                    try:
                        if not eval(f, {'ds': ds}):
                            logger.info(f'Skipping {ds.SOPInstanceUID} due to not matching filter {f}')
                            return
                    except Exception as filter_exc:
                        logger.info(f'Filter {f} failed due to {filter_exc}')
                        return False
                package_dicom(ds, anonymize=self.anonymize, compress=self.args.compress)
                for dst in self.args.dst:
                    dst.store(ds)
                if hasattr(self.args, "auth"):
                    self.upload(ds, params)
                extracted[key] = True
                if self.args.csv_out:
                    with open(self.args.csv_out, 'a', newline='') as f:
                        csv.writer(f).writerow(key)
            if path and self.args.delete_original:
                path.unlink()
        except Exception as exc:
            if isinstance(exc, InvalidDicomError):
                logger.debug(f'Error during process call: {exc}')
            else:
                logger.warning(f'Error during process call: {exc}')
                logger.debug(''.join(traceback.format_tb(exc.__traceback__)))
            if self.args.save_failed and self.f:
                try:
                    ts = datetime.datetime.now().strftime("%Y-%m%d-%H%M%S-")
                    dst = Pathy.fluid(self.args.save_failed) / f'{ts}{uuid.uuid4()}.dcm'
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    self.f.seek(0)
                    with dst.open('wb') as f:
                        f.write(self.f.read())
                except Exception as e:
                    logger.error(f'Error saving failed: {e}')
                    logger.debug(traceback.format_tb(e.__traceback__))
            raise exc
        finally:
            if self.f:
                self.f.close()


def handle_store(event, handler):
    """Handle EVT_C_STORE events."""
    f = io.BytesIO()
    f.write(b'\x00' * 128)
    f.write(b'DICM')
    # Encode and write the File Meta Information
    write_file_meta_info(f, event.file_meta)
    # Write the encoded dataset
    f.write(event.request.DataSet.getvalue())
    f.seek(0)
    primitive = event.assoc.requestor.primitive
    called = primitive.called_ae_title
    calling = primitive.calling_ae_title
    handler.handle(f=f, called_ae_title=called, calling_ae_title=calling)
    return 0x0000


def extracted_list(path):
    path = path and Pathy.fluid(path)
    if path and path.is_file():
        with path.open() as f:
            return {tuple(row) for row in csv.reader(f)}


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        return s.getsockname()[0]
    except Exception:
        return '127.0.0.1'
    finally:
        s.close()


def read_args(args=None):
    parser = argparse.ArgumentParser('EchoLoader')
    parser.add_argument(
        "--src",
        help="Source folder")
    parser.add_argument(
        "--src-details",
        help="Regular expression to apply on path to extract patient details used in the upload request. "
             "Can use (?P<key>re) to capture regular expression re to key. "
             "Key can be trial, patient_id, visit_id or filename")
    parser.add_argument(
        "--dst",
        nargs='+',
        default=[],
        help="Destination folder or DICOM destination")
    parser.add_argument(
        "--watch", action="store_true",
        help="Watch the src folder for changes")
    parser.add_argument(
        "--watch-sub-dirs", action="store_true",
        help="Watch only sub directories for changes")
    parser.add_argument(
        "--pacs", action="store_true",
        help="Starts PACS server")
    parser.add_argument(
        "--secure", nargs=3,
        help="Enable Secure PACS, must include 3 arguments which are paths to: "
             "CA certificate, server certificate and server key")
    parser.add_argument(
        "--pacs-ae-title", default=DEFAULT_AE_TITLE,
        help="PACS AE Title, defaults to Us2.ai")
    parser.add_argument(
        "--pacs-port", default=DEFAULT_PORT, type=int,
        help="PACS port, defaults to 11112")
    parser.add_argument(
        "--delete_original", action="store_true",
        help="Delete original files after processing")
    parser.add_argument(
        "--n", type=int, default=4,
        help="Number of workers")
    parser.add_argument(
        "--upload", action='store_true',
        help="Upload processed images to Us2.ai")
    parser.add_argument(
        "--upload-retries", default=3, type=int,
        help="Number of retries for upload")
    parser.add_argument(
        "--upload-retry-interval", default=5, type=int,
        help="Interval between retries for upload")
    parser.add_argument(
        "--env",
        help="The Us2.ai environment to use")
    parser.add_argument(
        "--extracted",
        help="File of cases to ignore - csv file with customer, trial, patientID, visit, filename")
    parser.add_argument(
        "--extracted-details",
        default=['SOPInstanceUID'],
        nargs="+",
        help="Details to use for matching extraction")
    parser.add_argument(
        "--csv-out",
        help="Path to csv file of extracted cases")
    parser.add_argument(
        "--verbose", action='store_true',
        help="Enable all application debug/info logs")
    parser.add_argument(
        "--save-failed", type=Pathy.fluid,
        help="Path to store failed cases locally")
    parser.add_argument(
        '--no-anonymization', action='store_false', dest='anonymize',
        help="No anonymization of data prior to upload",
    )
    parser.add_argument(
        '--pseudonymize', nargs='+',
        help="DCM tags to pseudonymize",
    )
    parser.add_argument(
        '--pseudonymize-file',
        help="Path to file for pseudonymization mapping",
    )
    parser.add_argument(
        '--no-compression', action='store_false', dest='compress',
        help="Don't compress videos into mp4 format",
    )
    parser.add_argument(
        '--customer',
        help="The customer tag used for the upload (Admin only)",
    )
    parser.add_argument(
        '--customer-aet',
        action='store_true',
        help="Whether or not customer should be derived from AET (Admin only)",
    )
    parser.add_argument(
        '--sync-mode',
        help="The sync mode to use, can be 'SIMPLE' or 'ADVANCED'",
        default='SIMPLE',
    )
    parser.add_argument(
        '--sync',
        nargs='+',
        default=[],
        help="Will try to sync structured report back to specified location."
             "Format: IP:PORT:REMOTE_AE_TITLE[:LOCAL_AE_TITLE:CERT:KEY][&MODALITIES]",
    )
    parser.add_argument(
        '--sync-url',
        default=False,
        action='store_true',
        help='Include url to measurement page in SR export',
    )
    parser.add_argument(
        '--sync-main-findings',
        default=False,
        action='store_true',
        help='Include main findings in SR export/DICOM encapsulated PDF',
    )
    parser.add_argument(
        '--sync-pdf-images',
        default=False,
        action='store_true',
        help='Include images in DICOM encapsulated PDF',
    )
    parser.add_argument(
        '--sync-designators',
        nargs='+',
        help='Designators used for SR export',
    )
    parser.add_argument(
        '--sync-modalities',
        default=['SR'],
        nargs='+',
        help='Modalities that should be synced to PACS, valid values are SR, PS, SC',
    )
    parser.add_argument(
        '--sync-poll',
        default=30,
        type=float,
        help='Delay between polls',
    )
    parser.add_argument(
        '--sync-stale',
        default=0,
        type=float,
        help='Number of seconds that exam needs to be stale before it is synced',
    )
    parser.add_argument(
        '--sync-from',
        default='datetime.datetime.utcnow()',
        help='The time point from which to sync, expression must return datetime',
    )
    parser.add_argument(
        '--sync-by-measurement',
        default=False,
        action='store_true',
        help='Will cause all PS/SC files to contain just one measurement each, instead of all for the frame',
    )
    parser.add_argument(
        '--sync-search',
        nargs='+',
        default=['reportCompleted=true'],
        help='Parameters for sync search, can be used to sync only when special criteria is met',
    )
    parser.add_argument(
        '--sync-mapping',
        help='Tag for custom mapping to use',
    )
    parser.add_argument(
        '--sync-regulatory-status',
        help='Will attach regulatory status in SR document',
        default=False,
        action='store_true',
    )
    parser.add_argument(
        '--sync-edited-status',
        help='Will attach measurement edit status in SR document',
        default=False,
        action='store_true',
    )
    parser.add_argument(
        '--sync-annotations',
        help='Will include measurement annotations and image references in SR document',
        default=False,
        action='store_true',
    )
    parser.add_argument(
        '--sync-generate-uid',
        help='Generate a random SOPInstanceUID instead of using the deterministic UID from the backend',
        default=False,
        action='store_true',
    )
    parser.add_argument(
        '-v',
        default='1.4.6',
        help='Version of API to use',
    )
    parser.add_argument(
        '-y',
        default=False,
        action='store_true',
        help='Answer yes to all prompts',
    )
    parser.add_argument(
        '--username',
        help='App username',
    )
    parser.add_argument(
        '--password',
        help='App password',
    )
    parser.add_argument(
        '--pacs-tls',
        default=False,
        action='store_true',
        help='Start PACS(TLS) server',
    )
    parser.add_argument(
        '--enforce-ae-title',
        default=False,
        action='store_true',
        help='Enforces that users have configured a proper AE title in the UI',
    )
    parser.add_argument(
        '--config-file',
        default=Pathy.fluid("config.json"),
        type=Pathy.fluid,
        help='Configuration file for the EchoLoader',
    )
    parser.add_argument(
        '--app-config',
        default=False,
        action='store_true',
        help='Read config from application(cloud/on-prem) instead of config file',
    )
    parser.add_argument(
        '--trial',
        help='Trial name of studies to upload',
    )
    parser.add_argument(
        '--proxy',
        help='Spin up a proxy against env on the given port',
        type=int,
    )
    parser.add_argument(
        '--log',
        help='File for logs',
    )
    parser.add_argument(
        '--filter',
        help='Inclusive filter for DS files to process',
        default=[
            'getattr(ds, "Modality", None) == "US"',  # Only accept ultrasound modalities
            'getattr(ds, "Manufacturer", None) != "Us2.ai"',  # Filter recursive cases
            'getattr(ds, "SequenceOfUltrasoundRegions", [])',  # Ensure ultrasound regions exists
            'getattr(ds.SequenceOfUltrasoundRegions[0], "PhysicalDeltaX", 0)',  # Ensure we have scale
        ],
        nargs='+',
    )
    parser.add_argument(
        '--src-glob',
        help='glob expression to apply on src directory',
        default='*',
    )
    parser.add_argument(
        '--params-trial',
        help='The dicom fields to check for trial',
        nargs='+',
        default=[],
    )
    parser.add_argument(
        '--params-pid',
        help='The dicom fields to check for patient ID',
        nargs='+',
        default=['PatientID'],
    )
    parser.add_argument(
        '--params-visit',
        help='The dicom fields to check for visit ID',
        nargs='+',
        default=['StudyID', 'StudyInstanceUID', 'StudyDate'],
    )
    parser.add_argument(
        '--trial-id',
        help='ID of the trial where all data should be uploaded',
    )
    parser.add_argument(
        '--use-echoloader-settings',
        action='store_true',
        help='Use the web application echoloader settings for anonymization',
    )
    args = parser.parse_args(sys.argv[1:] if args is None else args)
    if args.config_file.is_file():
        with args.config_file.open() as f:
            for k, v in json.load(f).items():
                setattr(args, k, v)

    env = args.env = (args.env and ENV(args.env)) or ENV('production')
    auth = None
    if args.upload or args.sync or args.proxy or args.app_config or args.enforce_ae_title:
        auth = args.auth = Us2Cognito(
            env.api_url,
            args.username or get_env_var('USERNAME', 'COGNITO_') or input("username: "),
            args.password or get_env_var('PASSWORD', 'COGNITO_') or getpass("password: "),
        )
        if args.env.cloud and (regions := auth.regions()):
            sep = '://'
            proto, domain = env.api_url.split(sep, 1)
            auth.api_url = args.env.api_url = f'{proto}{sep}{regions[0]}.{domain}'

    if args.app_config:
        logger.warning('Reading app config')
        user = auth.user
        args.app_config = user.get('dicom_router_config', {}).get('general', {})
        for k, v in args.app_config.items():
            try:
                if isinstance(v, str) and v.startswith('['):
                    v = ast.literal_eval(v)
                setattr(args, k, v)
            except Exception as exc:
                logger.error(f'Failed to read app param {k} - {v} due to {exc}')
                continue
        if args.use_echoloader_settings and (echoloader_settings := user.get('echoloader_settings')):
            args.anonymize, args.pseudonymize = anonymize_settings(user, (args.anonymize, args.pseudonymize))
            args.trial_id = args.trial_id or echoloader_settings.get('trial_id')
    args.customer = args.customer or (auth.customer() if auth and not args.customer_aet else None)
    args.src = args.src and Pathy.fluid(args.src)
    entries = (args.extracted and extracted_list(args.extracted)) or set()
    manager = Manager()
    args.extracted = manager.dict()
    for e in entries:
        args.extracted[e] = True
    args.dst = [detail_to_store(c, sync_modalities=args.sync_modalities, ae_title=args.pacs_ae_title)
                for c in args.dst]
    setup_logging(args.log, args.verbose)
    return args


def start_pacs_server(port, ae_title, handler, secure=None):
    if (secure and len(secure) != 3) or (secure and len(secure) == 3 and (not secure[1] or not secure[2])):
        logger.warning('No server certificate provided, unable to start PACS server with TLS')
        return

    logger.warning(f"Starting PACS{' (TLS)' if secure else ''} server on {get_ip()}:{port} with AE title {ae_title}")
    handlers = [(evt.EVT_C_STORE, handle_store, [handler])]
    ae = AE(ae_title)
    for sop in UID_dictionary.keys():
        ae.add_supported_context(sop, ALL_TRANSFER_SYNTAXES)
    ae.maximum_pdu_size = 0

    logger.warning('Setting up secure PACS connection') if secure else None

    try:
        return ae.start_server(
            ('0.0.0.0', port),
            block=False,
            ssl_context=server_context(*secure) if secure else None,
            evt_handlers=handlers,
        )
    except Exception as exc:
        logger.error(f'Failed to start PACS server due to {exc}')


def main():
    while True:
        args = read_args()
        handler = Handler(args)
        sync = observer = pacs = pacs_tls = httpd = None
        try:
            src = args.src
            if src and args.watch_sub_dirs:
                logger.info(f"watching for new directories in {os.path.abspath(src)}")
                src.mkdir(exist_ok=True, parents=True)
                observer = PollingObserver()
                dir_handler = DirHandler(handler)
                observer.schedule(dir_handler, src, recursive=False)
                observer.start()
                src = max((d for d in src.glob('*') if d.is_dir()), default=None, key=os.path.getmtime)
            if src:
                func = handler.watch if args.watch or args.watch_sub_dirs else handler.handle_existing_files
                func(src)
            if args.sync or args.sync_mode == 'ADVANCED':
                sync = Sync(args, handler.pool)
                sync.start()
            if args.pacs:
                pacs = start_pacs_server(
                    port=args.pacs_port, ae_title=args.pacs_ae_title, handler=handler, secure=args.secure)
            if args.pacs_tls:
                try:
                    certs = tls_certs()
                    tls_ae_title = get_env_var("SCP_AE_TITLE") or DEFAULT_AE_TITLE
                    tls_port = get_env_var("SCP_PORT") or DEFAULT_TLS_PORT
                    tls_port = int(tls_port) if isinstance(tls_port, str) and tls_port.isdecimal() else DEFAULT_TLS_PORT
                    if tls_port == args.pacs_port:
                        raise ValueError(f'Cloud PACS port {tls_port} is the same as local PACS port {args.pacs_port}')
                    pacs_tls = start_pacs_server(
                        port=tls_port, ae_title=tls_ae_title, handler=handler, secure=certs)
                except Exception as exc:
                    logger.error(f'Failed to start PACS(TLS) server due to {exc}')
            if args.proxy:
                httpd = ThreadingHTTPServer(server_address=('0.0.0.0', args.proxy),
                                            RequestHandlerClass=create_proxy(args))
                thread = threading.Thread(target=httpd.serve_forever)
                thread.start()
            while observer or handler.processing() or sync or pacs or pacs_tls or httpd:
                gc.collect()
                if args.app_config and args.auth:
                    app_config = None
                    try:
                        args.auth.get_user()
                        app_config = args.auth.user.get('dicom_router_config', {}).get('general', {})
                    except Exception as exc:
                        logger.error(f'Failed to get user due to {exc}')

                    if app_config and app_config != args.app_config:
                        logger.warning('Configuration updated')
                        logger.warning(f'Old configuration: {json.dumps(args.app_config)}')
                        logger.warning(f'New configuration: {json.dumps(app_config)}')
                        raise ConfigUpdatedException()
                time.sleep(5)
            break
        except KeyboardInterrupt:
            break
        except ConfigUpdatedException:
            pass
        finally:
            to_wait = [handler, observer, sync]
            to_wait = [e for e in to_wait if e]
            for e in to_wait:
                e.stop()
            for server in [pacs, pacs_tls, httpd]:
                if server:
                    server.shutdown()
            for e in to_wait:
                e.join()
            logger.warning('Shut down')
