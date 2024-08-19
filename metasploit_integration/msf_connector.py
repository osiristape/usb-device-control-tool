import xmlrpc.client
import logging
from metasploit_integration.logger import setup_logger

logger = setup_logger()

class MSFConnector:
    def __init__(self, host, port, token):
        self.url = f"http://{host}:{port}/api/"
        self.token = token
        self.client = None

    def connect(self):
        try:
            self.client = xmlrpc.client.ServerProxy(self.url)
            self.client.call('auth.login', self.token)
            logger.info("Connected to Metasploit RPC server.")
        except Exception as e:
            logger.error(f"Failed to connect to Metasploit RPC server: {str(e)}")
