# coding: utf-8
from unittest import TestCase
from os import path
from deployv.helpers import container, configuration_helper
from deployv.helpers import json_helper


class TestContainer(TestCase):

    def setUp(self):
        self.files_path = path.join(path.dirname(__file__), 'files')
        config_path = path.join(self.files_path, 'config.json')
        self.config = configuration_helper.DeployvConfig(deploy_config=config_path)
        self.container_config = self.config.container_config

    def test_generate_hostname(self):
        ''' Use the configuration from the config.json file and use it
        to call the generate_hostname method, then verify that the
        result has the expected format
        '''
        res = container.generate_hostname(self.config)
        self.assertEqual(res, ('{tid}{cid}.{domain}'
                               .format(tid=self.config.instance_config['task_id'],
                                       cid=self.config.instance_config['customer_id'],
                                       domain=self.container_config['domain'])))

    def test_wrong_hostname(self):
        ''' Use the configuration from the config.json file and use it
        to call the generate_hostname method, all the _ must be removed:
        https://github.com/docker/docker/issues/20371
        '''
        self.config.instance_config.update({'customer_id': 'some_customer'})
        res = container.generate_hostname(self.config)
        self.assertNotIn('_', res)

    def test_generate_binds(self):
        ''' Use the volumes from the config.json to generate binds and compare
        the result with the expected binds
        '''
        user_home = path.expanduser('~')
        expected_value = {
            "{home}/tmp".format(home=user_home): {
                "bind": "/tmp",
                "ro": False
                },
            "{home}/logs".format(home=user_home): {
                "bind": "/var/log/supervisor",
                "ro": False
                },
            "{home}/ssh".format(home=user_home): {
                "bind": "/home/odoo/.ssh",
                "ro": False
                },
            "{home}/filestore".format(home=user_home): {
                "bind": "/home/odoo/.local/share/Odoo",
                "ro": False
                }
            }
        res = container.generate_binds(self.container_config['volumes'], user_home)
        self.assertEqual(expected_value, res)

    def test_generate_prefix(self):
        ''' Generate a prefix using the generate_prefix method and make sure it
        has the format task_id_customer_id
        '''
        prefix = container.generate_prefix(self.config)
        self.assertEqual(prefix, '{tid}_{cid}'.format(
            tid=self.config.instance_config['task_id'],
            cid=self.config.instance_config['customer_id']))

    def test_generate_prefix_with_prefix(self):
        self.config.prefix = 'test'
        prefix = container.generate_prefix(self.config)
        self.assertEqual(prefix, self.config.prefix)

    def test_generate_env_vars(self):
        ''' Use the env_vars in config.json to call the method generate_env_vars
        and then check that the result has the expected format with the values
        specified in the env_vars configuration
        '''
        expected = []
        env_vars = self.container_config['env_vars']
        for key, val in env_vars.items():
            expected.append('{key}={val}'.format(key=key.upper(), val=val))
        env_vars = container.generate_env_vars(env_vars)
        self.assertEqual(env_vars, expected)

    def test_generate_port_lists(self):
        ''' Use the dict with the ports in the config.json to use them as parameters
        for the generate_port_lists method, then verify that the returned list contains
        the keys of the given dict
        '''
        expected = []
        for key in self.container_config['ports']:
            expected.append(int(key))
        ports = container.generate_port_lists(self.container_config['ports'])
        self.assertEqual(ports, expected)

    def test_get_ports_dict(self):
        net_path = path.join(self.files_path, 'network_settings.json')
        networking_settings = json_helper.load_json(net_path)
        res = container.get_ports_dict(networking_settings)
        self.assertDictEqual({'8072': 32768, '8069': 8069}, res)
        res = container.get_ports_dict({'NetworkSettings': {'Ports': {}}})
        self.assertDictEqual({}, res)

    def test_parse_env_vars(self):
        env_vars = ['HOME=/home', 'INSTANCE=test']
        expected_res = {'home': '/home', 'instance': 'test'}
        res = container.parse_env_vars(env_vars)
        self.assertIsInstance(res, dict)
        self.assertEqual(res, expected_res)
