import base64
import logging

import requests

from echoloader.lib.hl7 import Hl7

logger = logging.getLogger('echolog')


class Hl7Sync:
    def __init__(self, study, **kwargs):
        self.study = study
        self.db_measurements = kwargs.get('measurements', {})
        self.hl7_config = kwargs.get('hl7_config', {})
        self.protocol = kwargs.get('protocol', {})
        self.api_url = kwargs.get('api_url', '')
        self.pdf_params = kwargs.get('pdf_params', {})
        self.headers = kwargs.get('headers', {})
        self.is_echoloader = kwargs.get('is_echoloader', True)
        self.pdf_retrieve_func = kwargs.get('pdf_retrieve_func')

    def read_measurements(self):
        measurements = {}
        for m in self.db_measurements.values():
            proto = self.protocol.get('measurements', {}).get(str(m.get('code_id')), {})
            if (proto.get('shouldDisplay')
                    and m.get('used')
                    and m.get('dicom_id')
                    and m.get('plot_obj')):
                measurements[m['code_id']] = {
                    "proto": proto,
                    "m_value": m,
                }
        return measurements

    def pdf(self, report_type):
        pdf_content = None

        try:
            if report_type == 'DOCX':
                self.pdf_params['report_type'] = report_type

            if self.is_echoloader:
                res = requests.get(f"{self.api_url}/study/pdf/{self.study.get('id')}", headers=self.headers,
                                   params=self.pdf_params)
                pdf_content = res.content if res.status_code == 200 else None
                if res.status_code != 200:
                    logger.error(f'Failed to fetch from {res.url} - {res.status_code}')
            elif self.pdf_retrieve_func:
                pdf_content = self.pdf_retrieve_func(self.pdf_params)

            return base64.b64encode(pdf_content).decode("utf-8") if pdf_content else None
        except Exception as exc:
            logger.error(f'Failed to fetch PDF due to {exc}')
            return None

    def sync_hl7(self):
        measurements = {}
        report_doc_encoded = None

        try:
            report_type = self.hl7_config.get('report_type', 'TEXT')
            if report_type in ['ALL', 'TEXT']:
                measurements = self.read_measurements()
            if report_type != "TEXT":
                report_doc_encoded = self.pdf(report_type)

            hl7 = Hl7(self.hl7_config, "ORU_R01", "2.5")
            msg_control_id = hl7.generate(self.study, measurements, report_type, report_doc_encoded)

            if msg_control_id:
                hl7.send()
            else:
                logger.warning(f'Failed to generate HL7 {msg_control_id}')
        except Exception as ex:
            logger.error(f'Failed to sync HL7 due to {ex}')
