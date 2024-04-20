import datetime
import logging
import threading
import time

import requests
from dateutil import parser

from echoloader.dimse import detail_to_destination
from echoloader.login import unpack
from echoloader.results_sync import ResultsSync

logger = logging.getLogger('echolog')


class Sync(threading.Thread):
    def __init__(self, cmd, pool, *vargs, **kwargs):
        super().__init__(*vargs, **kwargs)
        self.args = cmd
        self.auth = cmd.auth
        self.api_url = self.auth.api_url
        self.uploader = self.auth.user['email']
        self.killed = False
        self.params = {'v': cmd.v}
        self.sync_from = eval(cmd.sync_from).replace(tzinfo=datetime.timezone.utc)
        self.last_sync = {}
        self.sync_stale = cmd.sync_stale and datetime.timedelta(seconds=cmd.sync_stale)
        self.modalities = cmd.sync_modalities
        self.sync_mode = cmd.sync_mode
        self.dicom_router_config = self.auth.user.get('dicom_router_config', {})
        self.poll = cmd.sync_poll
        self.pool = pool
        self.search_params = {k: v for e in cmd.sync_search for k, v in [e.split('=', 1)]}

        self.sync_destinations = []
        self.protocol = unpack(requests.get(
            f'{self.api_url}/sync/protocol', params=self.params, headers=self.auth.get_headers()))['current_protocol']
        self.set_sync_destinations()

    def set_sync_destinations(self):
        if self.sync_mode == 'ADVANCED':
            sync_destination_params = {
                **self.params,
                'request_from': 'ECHOLOADER_CLIENT',
            }
            self.sync_destinations = unpack(requests.get(
                f'{self.api_url}/sync/destination', params=sync_destination_params, headers=self.auth.get_headers()))
        else:
            sync_modalities = self.modalities
            sync_modalities = sync_modalities if len(sync_modalities) > 0 else ['SR']
            for sync_details in self.args.sync:
                self.sync_destinations.append(detail_to_destination(
                    sync_details, sync_modalities=sync_modalities, ae_title=self.args.pacs_ae_title))

    def stop(self):
        self.killed = True

    def handle_study_sync_error(self, err, sid):
        logger.error(f'Failed to sync study {sid} due to {err}')

    def sync(self):
        if len(self.sync_destinations) == 0:
            logger.warning('No sync destinations specified, skipping sync')
            return

        filter_params = {
            **self.params,
            'uploader': self.uploader,
            'lastUpdatedFrom': max([self.sync_from, *self.last_sync.values()]),
            **self.search_params,
        }
        now = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
        res = unpack(
            requests.get(f'{self.api_url}/study/search', params=filter_params, headers=self.auth.get_headers()), {})
        results = res.get('results', [])
        for study in results:  # All search results have been updated since we last checked -> sync everything
            sid = study['id']
            last_sync = self.last_sync.get(sid, self.sync_from)
            creation = parser.parse(study['lastUpdatedAt']).replace(tzinfo=datetime.timezone.utc)

            if self.sync_stale and creation + self.sync_stale > now:
                logger.info(f'skipping sync for {sid} as it has been updated in the last {self.args.sync_stale}s '
                            f'last update at {creation}')
                continue
            self.last_sync[sid] = creation
            logger.info(f'Syncing {sid} for changes since {last_sync}')

            kwargs = {
                'protocol': self.protocol,
                'last_sync': last_sync,
                'params': self.params,
                'api_url': self.api_url,
                'headers': self.auth.get_headers(),
                'sync_source': 'ECHOLOADER',
                'sync_event': 'REAL_TIME',
                'sync_mode': self.sync_mode,
                'sync_destinations': self.sync_destinations,
                'dicom_router_config': self.auth.user.get('dicom_router_config', {}),
            }

            results_sync = ResultsSync(study, vars(self.args), **kwargs)
            self.pool.apply_async(results_sync.sync_results,
                                  error_callback=lambda err: self.handle_study_sync_error(err, sid))

    def run(self) -> None:
        while not self.killed:
            try:
                self.sync()
            except Exception as exc:
                logger.error(f'Failed sync due to: {exc}')
            time.sleep(self.poll)
