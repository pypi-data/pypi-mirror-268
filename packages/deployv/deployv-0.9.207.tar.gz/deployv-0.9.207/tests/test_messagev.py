# coding: utf-8
from deployv.messaging import basemsg
from deployv.helpers import json_helper
from unittest import TestCase


class TestMessageV(TestCase):

    def test_default(self):
        message = basemsg.BasicMessage()
        message.sender_node_id = 'me01'
        message.receiver_node_id = 'you01'
        res = message.build_message()
        validation = json_helper.validate_schema(
            res, schema=json_helper.build_schema('deploy.deploy'))
        self.assertFalse(validation.get("result"))
        self.assertIn('{} is not valid under any of the given schemas', validation.get("error"))
        message.set_message_body({"command": "restore", "result": "ok"}, "result")
        res = message.build_message()
        validation = json_helper.validate_schema(res)
        self.assertFalse(validation.get("error"))
        self.assertIsInstance(message.get_message_str(), str)

    def test_ack(self):
        message = basemsg.BasicMessage()
        message.sender_node_id = 'me01'
        message.receiver_node_id = 'you01'
        message.set_command('system.ls', {'p1': '-a'})
        message_ack = message.get_ack_message()
        builded_ack = message_ack.build_message()
        validation = json_helper.validate_schema(builded_ack)
        self.assertFalse(validation.get("error"))
        self.assertEqual(message.sender_node_id, builded_ack.get('receiver_node_id'))
        self.assertEqual(message.receiver_node_id, builded_ack.get('sender_node_id'))
        self.assertNotEqual(message.message_id, builded_ack.get('message_id'))
        self.assertEqual(message.message_id, builded_ack.get('response_to'))
