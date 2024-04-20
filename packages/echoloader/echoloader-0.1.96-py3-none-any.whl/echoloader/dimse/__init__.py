import uuid

from echoloader.dimse.dimse import Dimse, DEFAULT_AE_TITLE
from echoloader.dimse.fs import DicomFs


def detail_to_destination(sync_details, **kwargs):
    details = sync_details.split('&')
    parts = details[0].split(':')
    sync_destination = {
        'id': str(uuid.uuid4()),
        'sync_modalities': details[1].split(',') if len(details) > 1 else kwargs.get('sync_modalities', ['SR']),
        'sync_source': 'ECHOLOADER',
    }
    if len(parts) == 1:
        sync_destination['path'] = parts[0]
    elif len(parts) > 2:
        sync_destination['host'] = parts[0]
        sync_destination['port'] = parts[1]
        sync_destination['remote_ae_title'] = parts[2]
        sync_destination['local_ae_title'] = parts[3] if len(parts) > 3 else kwargs.get('ae_title')
        sync_destination['anonymous_tls'] = False
        sync_destination['enable_tls'] = False
        sync_destination['client_ca_cert'] = None
        sync_destination['server_cert'] = None
        sync_destination['server_key'] = None
        if len(parts) > 5:
            ca, cert, key = parts[4:7] if len(parts) > 5 else (None, None, None)
            sync_destination['enable_tls'] = True
            sync_destination['anonymous_tls'] = not cert or not key
            sync_destination['client_ca_cert'] = ca
            sync_destination['server_cert'] = cert
            sync_destination['server_key'] = key
    return sync_destination


def destination_to_store(sync_destination):
    if 'path' in sync_destination:
        return DicomFs(sync_destination)
    return Dimse(sync_destination)


def detail_to_store(sync_details, **kwargs):
    return destination_to_store(detail_to_destination(sync_details, **kwargs))


__all__ = [detail_to_store, destination_to_store, detail_to_destination, DEFAULT_AE_TITLE]
