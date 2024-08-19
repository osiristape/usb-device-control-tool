import logging
from metasploit_integration.ms_connector import MSFConnector

logger = setup_logger()

class PayloadGenerator:
    def __init__(self, msf_connector):
        self.msf_connector = msf_connector

    def generate_payload(self, payload_type, options):
        try:
            payload = self.msf_connector.client.call('module.execute', 'payloads', payload_type, options)
            logger.info(f"Generated payload: {payload}")
            return payload
        except Exception as e:
            logger.error(f"Failed to generate payload: {str(e)}")
            return None
