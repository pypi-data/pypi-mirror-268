# coding: utf-8
from unittest import TestCase
from deployv.helpers import configuration_helper, utils
from configparser import ConfigParser


class TestConfiguration(TestCase):

    def test_parse_config(self):
        new_config = ConfigParser()
        new_config.add_section('test_section')
        new_config.set('test_section', 'test_int', '1')
        new_config.set('test_section', 'test_bool', 'yes')
        new_config.set('test_section', 'test_str', 'test')
        with open('test_configuration_file.conf', 'w') as config_file:
            new_config.write(config_file)
        config_cls = configuration_helper.DeployvConfig(
            worker_config='test_configuration_file.conf')
        self.assertIsInstance(config_cls.rmq, dict)
        self.assertIsInstance(config_cls.deployer, dict)
        self.assertIsInstance(config_cls.postgres, dict)
        self.assertEqual(int(config_cls.test_section.get('test_int')), 1)
        self.assertTrue(config_cls.test_section.get('test_bool'))
        self.assertEqual(config_cls.test_section.get('test_str'), 'test')
        utils.clean_files(['test_configuration_file.conf'])
