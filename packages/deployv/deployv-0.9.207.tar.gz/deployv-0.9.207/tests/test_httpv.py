# coding: utf-8
import mock
from unittest import TestCase
from configparser import ConfigParser
from deployv.helpers import configuration_helper
from deployv.messaging.http import httpv, receiverv, senderv, worker
from os.path import join, dirname


class RequestResponse(object):

    @staticmethod
    def json():
        return {'result': {'res': True}}

    @property
    def status_code(self):
        return 200


class BadRequestResponse(object):

    @staticmethod
    def json():
        return {
            'result': {
                'error': {
                    'code': 400,
                    'message': 'Some error'
                }
            }
        }

    @property
    def status_code(self):
        return 400


class EmptyRequestResponse(object):

    @staticmethod
    def json():
        return {}

    @property
    def status_code(self):
        return 200


class TestHttpV(TestCase):

    def setUp(self):
        self.raw_config = ConfigParser()
        config_path = join(dirname(__file__), 'files/test_deployv.conf')
        self.raw_config.read(config_path)
        self.config = configuration_helper.DeployvConfig(worker_config=config_path)
        self.config_cls = httpv.FileHttpConfiguration(self.config)
        self.receiver = receiverv.HttpReceiverV(self.config_cls, 'testworker01')
        self.sender = senderv.HttpSenderV(self.config_cls, 'testworker01')
        self.worker = worker.HttpWorker(self.config_cls, receiverv.HttpReceiverV,
                                        senderv.HttpSenderV, 'testworker01')

    def _callback(self, msg):
        self.assertTrue(msg.get('res'))

    def test_get_result_object(self):
        res = self.config_cls.get_result_object()
        self.assertIsInstance(res, httpv.FileHttpConfiguration)

    def test_wrong_config(self):
        with self.assertRaises(ValueError):
            httpv.FileHttpConfiguration('config')

    @mock.patch('requests.get', return_value=RequestResponse())
    def test_http_receiver_get_message(self, mocked_request):
        self.receiver.get_message(self._callback)

    def test_http_receiver_get_message_errors(self):
        res = self.receiver.get_message(self._callback)
        self.assertFalse(res)
        with mock.patch('requests.get', return_value=EmptyRequestResponse()):
            res = self.receiver.get_message(self._callback)
            self.assertFalse(res)
        with mock.patch('requests.get', return_value=BadRequestResponse()):
            res = self.receiver.get_message(self._callback)
            self.assertFalse(res)

    @mock.patch('deployv.messaging.http.receiverv.HttpReceiverV.get_message')
    def test_receiver_stop(self, mocked_msg):
        self.receiver.stop()
        self.assertFalse(self.receiver.active)

    @mock.patch('requests.post')
    def test_senderv_send_message(self, mocked_post):
        self.sender.send_message({'result': 'message'})
        self.assertTrue(mocked_post.called)
