# coding: utf-8

import os
import simplejson
from unittest import TestCase
from deployv.helpers import json_helper, utils


class TestJsonHelper(TestCase):

    def setUp(self):
        base_path = os.path.join(os.path.dirname(__file__), 'files')
        self.json_file = os.path.join(base_path, 'config.json')
        self.msg_file = os.path.join(base_path, 'message.json')
        self.demo_dict = {
            "prop1": 123,
            "prop2": {
                "prop3": "test"
            }
        }
        self.schema = {
            "type": "object",
            "properties": {
                "prop1": {
                    "type": "integer",
                },
                "prop2": {
                    "type": "object",
                    "properties": {
                        "prop3": {
                            "type": "string"
                        }
                    },
                    "required": ["prop3"]
                }
            },
            "required": ["prop1", "prop2"]
        }

    @property
    def config_dict(self):
        config_dict = json_helper.load_json_file(self.json_file)
        return config_dict

    @property
    def msg_dict(self):
        msg_dict = json_helper.load_json_file(self.msg_file)
        msg_dict.get('message_body').update({
            'parameters': self.config_dict
        })
        return msg_dict

    @property
    def schema_deploy(self):
        return json_helper.build_schema(model='deploy.deploy')

    def test_10_load_json_str(self):
        """Test the load_json method passing a string.
        """
        demo_json = simplejson.dumps(self.demo_dict)
        # Should return the same dict as self.demo_dict
        json_dict = json_helper.load_json(demo_json)
        self.assertIsInstance(json_dict, dict)
        self.assertEqual(json_dict, self.demo_dict)

    def test_20_load_json_file(self):
        """Test the load_json method passing a file path. It should return a
        dictionary with the file.
        """
        with open(self.json_file) as json_file:
            original_json = simplejson.loads(json_file.read())
        # Should return the same dict inside the json file
        loaded_json = json_helper.load_json(self.json_file)
        self.assertIsInstance(loaded_json, dict)
        self.assertEqual(original_json, loaded_json)

    def test_30_load_json_dict(self):
        """Test the load_json method passing a dict. It should return the same
        dictionary.
        """
        # Should return the same dict that is being passed
        json_dict = json_helper.load_json(self.demo_dict)
        self.assertIsInstance(json_dict, dict)
        self.assertEqual(json_dict, self.demo_dict)

    def test_40_load_json_error(self):
        """Test the load_json method passing an invalid param.
        """
        # Should fail because the string is not a valid json
        json = json_helper.load_json("{")
        self.assertFalse(json)

    def test_50_build_schema(self):
        """Tests the build_schema method.
        """
        # Should return the base schema
        schema = json_helper.build_schema()
        self.assertIsInstance(schema, dict)
        # Should still return the base schema if the schema is not found
        schema_notfound = json_helper.build_schema(model='notfound')
        self.assertEqual(schema, schema_notfound)
        # Should return the extended schema
        self.assertIsInstance(self.schema_deploy, dict)
        self.assertNotEqual(schema, self.schema_deploy)

    def test_60_validate_schema_ok(self):
        """Test the validate_schema method with a valid dict.
        """
        # Should return that is valid and no error message
        validation = json_helper.validate_schema(self.demo_dict, self.schema)
        self.assertTrue(validation.get("result"))
        self.assertFalse(validation.get("error"))
        validation = json_helper.validate_schema(self.msg_dict, self.schema_deploy)
        self.assertTrue(validation.get("result"))
        self.assertFalse(validation.get("error"))

    def test_70_validate_schema_ko(self):
        """Test the validate_schema method with an invalid dict.
        """
        # Should return that is not valid and the error message
        validation = json_helper.validate_schema({}, self.schema)
        self.assertFalse(validation.get("result"))
        self.assertTrue(validation.get("error"))
        validation = json_helper.validate_schema(self.demo_dict, self.schema_deploy)
        self.assertFalse(validation.get("result"))
        self.assertTrue(validation.get("error"))

    def test_80_save_json(self):
        ''' Load a json file using load_json method, save the results in another json file
        and make sure the file is created and contains the same content as the original
        '''
        res = json_helper.save_json(self.demo_dict, 'test.json')
        self.assertTrue(os.path.isfile(res))
        saved_json = json_helper.load_json('test.json')
        self.assertEqual(self.demo_dict, saved_json)
        utils.clean_files('test.json')

    def test_90_save_json_exception(self):
        ''' Try to use save_json method to save a string in a folder in order to get an IOError,
        if the error is correctly handled this method will return False
        '''
        res = json_helper.save_json('test', 'tests/')
        self.assertFalse(res)
