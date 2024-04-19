# coding: utf-8
import os
from mock import patch, Mock
from unittest import TestCase
from deployv.base import dockerv
from deployv.helpers import json_helper
from deployv.base import errors


def _mocked_inspect(container_id):
    if container_id == 1:
        ports = {"NetworkSettings": {
            "Ports": {
                "22/tcp": [{"HostIp": "0.0.0.0",
                            "HostPort": "30007"}],
                "5432/tcp": [{"HostIp": "127.0.0.1",
                              "HostPort": "30006"}],
                "8069/tcp": [{"HostIp": "0.0.0.0",
                              "HostPort": "30008"}],
                "8072/tcp": [{"HostIp": "0.0.0.0",
                              "HostPort": "30009"}]
            }}}
        return ports
    elif container_id == 2:
        ports = {"NetworkSettings": {
            "Ports": {
                "22/tcp": [{"HostIp": "0.0.0.0",
                            "HostPort": "30010"}],
                "5432/tcp": [{"HostIp": "127.0.0.1",
                              "HostPort": "30011"}],
                "8069/tcp": [{"HostIp": "0.0.0.0",
                              "HostPort": "30008"}],
                "8072/tcp": [{"HostIp": "0.0.0.0",
                              "HostPort": "30009"}]
            }}}
        return ports


class TestUtils(TestCase):

    @patch('deployv.base.dockerv.DockerClient')
    @patch('deployv.base.dockerv.Client')
    def setUp(self, mocked_api, mocked_docker):
        config_path = os.path.join(os.path.dirname(__file__), 'files',
                                   'config.json')
        config = json_helper.load_json(config_path)
        self.dockerv = dockerv.DockerV(config.get('container_config'))

    def test_01_parse_ports(self):
        """Test the `_parse_ports` method to make sure that it obtains the
        correct ports in any of the formats returned by the `get_ports_dict`
        method.
        """
        ports = {
            '8069': ['127.0.0.1:8069', '1.2.3.4:8069'],
            '5432': ['172.17.0.1:32300'],
            '8072': 33500
        }
        res = self.dockerv._parse_ports(ports)
        self.assertEqual(sorted(res), sorted([32300, 33500, 8069]))

    def test_02_get_used_ports(self):
        """Verify that the `_get_used_ports` method returns the ports used by
        all the containers despite if the have ssh access or not.


        """
        container_1 = Mock()
        container_1.id = 1
        container_2 = Mock()
        container_2.id = 2
        self.dockerv.__cli2 = Mock()
        self.dockerv.cli2.containers.list.return_value = [container_1, container_2]
        self.dockerv.inspect = Mock()
        self.dockerv.inspect = _mocked_inspect
        res = self.dockerv._get_used_ports()
        self.assertEqual(sorted(res), sorted([30006, 30007, 30008, 30009, 30010, 30011]))

    def test_03_set_default_ports(self):
        """Verify that the `set_default_ports` method uses the specified ports
        if they are free and that it changes them correctly if they are not.
        """
        container_1 = Mock()
        container_1.id = 1
        container_2 = Mock()
        container_2.id = 2
        self.dockerv.__cli2 = Mock()
        self.dockerv.cli2.containers.list.return_value = [container_1, container_2]
        self.dockerv.inspect = Mock()
        self.dockerv.inspect = _mocked_inspect
        used_ports = [30006, 30007, 30008, 30009, 30010, 30011]
        self.dockerv._InstanceV__full_config = Mock()
        # Test with no ports available
        self.dockerv._InstanceV__full_config.deployer = {
            'docker_start_port': 30006, 'docker_end_port': 30010}
        original_ports = self.dockerv.config.get('ports').copy()
        self.dockerv.config.update({'ports': {}})
        with self.assertRaises(errors.ErrorPort):
            self.dockerv.set_default_ports()
        # Reset the available ports
        self.dockerv._InstanceV__full_config.deployer = {}
        self.dockerv.config.update({'ports': original_ports})
        # Test with specific available ports and a dev instance
        self.dockerv._InstanceV__full_config.instance_config = {
            'instance_type': 'develop'}
        self.dockerv.config.update({'ports': {'8069': 30001, '8072': 30002}})
        self.dockerv.set_default_ports()
        self.assertEqual(sorted(self.dockerv.config.get('ports').values()),
                         sorted([30001, 30002]))
        # Test with random ports and a dev instance
        self.dockerv.config.update({'ports': {'8069': 0, '8072': 0}})
        self.dockerv.set_default_ports()
        for port in self.dockerv.config.get('ports'):
            self.assertTrue(port not in used_ports)
        # Test with used ports and a dev instance
        self.dockerv.config.update({'ports': {'8069': 30010, '8072': 30011}})
        self.dockerv.set_default_ports()
        for port in self.dockerv.config.get('ports'):
            self.assertTrue(port not in used_ports)
        # Test with specific available ports and an instance != dev
        self.dockerv._InstanceV__full_config.instance_config = {
            'instance_type': 'test'}
        self.dockerv.config.update({'ports': {'8069': 30001, '8072': 30002}})
        self.dockerv.set_default_ports()
        self.assertEqual(sorted(self.dockerv.config.get('ports').values()),
                         sorted([30001, 30002]))
        # Test with random ports and an instance != dev
        self.dockerv.config.update({'ports': {'8069': 0, '8072': 0}})
        self.dockerv.set_default_ports()
        for port in self.dockerv.config.get('ports'):
            self.assertTrue(port not in used_ports)
        # Test with used ports and an instance != dev
        self.dockerv.config.update({'ports': {'8069': 30010, '8072': 30011}})
        self.dockerv.set_default_ports()
        self.assertEqual(sorted(self.dockerv.config.get('ports').values()),
                         sorted([30010, 30011]))
