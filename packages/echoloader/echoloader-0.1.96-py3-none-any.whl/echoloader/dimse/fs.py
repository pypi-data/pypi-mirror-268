import logging

from pathy import Pathy

from echoloader.dimse.store import Store

logger = logging.getLogger('echolog')


class DicomFs(Store):
    def __init__(self, sync_destination):
        super().__init__(sync_destination)
        self.dst = sync_destination['path']

    def store(self, ds, *_):
        try:
            logger.debug(f"Storing {ds.SOPInstanceUID} to {self.dst}")

            dst = Pathy.fluid(self.dst) / ds.PatientID / f"{ds.SOPInstanceUID}.dcm"
            dst.parent.mkdir(exist_ok=True, parents=True)
            with dst.open('wb') as f:
                ds.save_as(f, write_like_original=False)
        except Exception as exc:
            raise ValueError(f"Failed to store {ds.SOPInstanceUID} to {self.dst} due to {exc}")

    def __str__(self):
        return f"Store {self.name}({self.id}) on file system at {self.dst}"
