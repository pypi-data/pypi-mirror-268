import logging

from pynetdicom import AE

from echoloader.dimse.store import Store
from echoloader.dimse.tls import tls_certs, client_context

logger = logging.getLogger('echolog')
DEFAULT_AE_TITLE = "Us2.ai"


class Dimse(Store):
    def __init__(self, sync_destination):
        super().__init__(sync_destination)
        self.anonymous_tls = False
        self.host = self.port = self.remote_ae_title = self.local_ae_title = self.cert = self.key = None
        self.ca = self.ca_data = None
        self.host = sync_destination.get('host')
        self.port = sync_destination.get('port')
        self.remote_ae_title = sync_destination.get('remote_ae_title')
        self.local_ae_title = sync_destination.get('local_ae_title', DEFAULT_AE_TITLE)
        self.anonymous_tls = sync_destination.get('anonymous_tls', False)

        if not self.host or not self.port or not self.remote_ae_title:
            raise ValueError('PACS sync has not been configured')

        self.port = int(self.port)
        if sync_destination.get('enable_tls', False):
            if sync_destination.get('sync_source') == 'ECHOLOADER':
                self.ca = sync_destination.get('client_ca_cert')
                if not self.anonymous_tls:
                    self.cert = sync_destination.get('server_cert')
                    self.key = sync_destination.get('server_key')
            else:
                self.ca_data = sync_destination.get('client_ca_data', '')
                if not self.anonymous_tls:
                    server_certs = tls_certs()
                    self.ca, self.cert, self.key = server_certs[:3] if len(server_certs) >= 3 else (None, None, None)

    def store(self, ds, called_ae=None):
        ae = AE(ae_title=self.local_ae_title)
        ae.add_requested_context(ds.SOPClassUID, ds.file_meta.TransferSyntaxUID)

        remote_ae = called_ae or self.remote_ae_title
        assoc = ae.associate(self.host, self.port, ae_title=remote_ae,
                             tls_args=(client_context(self), None) if self.cert or self.ca_data else None)

        if not assoc.is_established:
            raise ConnectionError('Association rejected, aborted or never connected')
        # Use the C-STORE service to send the dataset
        # returns the response status as a pydicom Dataset
        try:
            # force treat context as supporting the SCP role
            for cx in assoc.accepted_contexts:
                cx._as_scp = True

            status = assoc.send_c_store(ds)

            # Check the status of the storage request
            if status:
                # If the storage request succeeded this will be 0x0000
                logger.debug(f'C-STORE request status: 0x{status.Status:04x}')
            else:
                raise ValueError('Connection timed out, was aborted or received invalid response')
        finally:
            # Release the association
            assoc.release()

    def __str__(self):
        return f"Send to PACS {self.name}({self.id}) {self.host}:{self.port}:{self.remote_ae_title}"
