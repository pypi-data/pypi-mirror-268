# coding: utf-8
from unittest import TestCase
from configparser import ConfigParser
import pika
from mock import patch
from deployv.helpers import json_helper, configuration_helper, utils
from deployv.messaging import basemsg
from deployv.messaging.rabbit import senderv, rabbitv
from os.path import join, dirname


class TestRabbitV(TestCase):

    def setUp(self):
        self.files_path = join(dirname(__file__), 'files')
        self.json_cfg = json_helper.load_json(join(self.files_path, 'rabbit_config.json'))
        self.config = join(self.files_path, 'test_config.conf')
        with open(self.config, 'w') as file_hd:
            config_hd = ConfigParser()
            config_hd.add_section('rmq')
            for key, value in self.json_cfg.items():
                config_hd.set('rmq', key, '' if not value else str(value))
            config_hd.write(file_hd)

    def tearDown(self):
        utils.clean_files(self.config)

    def _check_config_values(self, config):
        self.assertIsInstance(config.parameters, pika.ConnectionParameters)
        self.assertIsInstance(config.credentials, pika.PlainCredentials)
        self.assertIsInstance(config.properties, pika.BasicProperties)
        self.assertEqual(config.user, self.json_cfg.get('rmq_user'))
        self.assertEqual(config.password, self.json_cfg.get('rmq_passwd'))
        self.assertEqual(config.route, self.json_cfg.get('rmq_task_topic'))
        self.assertEqual(config.exchange_name, self.json_cfg.get('rmq_exchange'))

    def test_file_config(self):
        config_class = configuration_helper.DeployvConfig(worker_config=self.config)
        config = rabbitv.FileRabbitConfiguration(config_class)
        self._check_config_values(config)

    def test_file_config_assert(self):
        with self.assertRaises(ValueError):
            rabbitv.FileRabbitConfiguration('non_existing_file.conf')

    @patch('pika.BlockingConnection')
    def test_send_task(self, mocked_class):
        mc = mocked_class.return_value
        mc.basic_publish.return_value = True
        config_class = configuration_helper.DeployvConfig(worker_config=self.config)
        config = rabbitv.FileRabbitConfiguration(config_class)
        sender = senderv.RabbitSenderV(config, 'me01')

        message = basemsg.BasicMessage()
        message.sender_node_id = 'me01'
        message.receiver_node_id = 'you01'
        message.set_command('system.ls', {'p1': '-a'})

        res = sender.send_message(message)
        self.assertTrue(mocked_class.called)
        self.assertIsInstance(res, str)
        self.assertTrue('parameters' in res)
        self.assertFalse('result' in res)
