import unittest
from unittest.mock import patch
from metasploit_integration.ms_connector import MSFConnector

class TestMSFConnector(unittest.TestCase):
    @patch('metasploit_integration.ms_connector.xmlrpc.client.ServerProxy')
    def test_connect(self, mock_server_proxy):
        connector = MSFConnector('localhost', 55552, 'token')
        connector.connect()
        mock_server_proxy.assert_called_with('http://localhost:55552/api/')
