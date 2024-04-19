# coding: utf-8
import logging
import types
import mock
import spur
import shlex
from datetime import datetime
from unittest import TestCase
import os
import base64
from deployv.helpers import utils, json_helper, configuration_helper
from mock import patch
from deployv.base import errors
from six import string_types
from tempfile import mkdtemp


class TestUtils(TestCase):

    def setUp(self):
        self.main_path = os.path.dirname(__file__)
        self.files_path = os.path.join(self.main_path, 'files')
        self.config_path = os.path.join(self.files_path, 'config.json')
        self.ssh_path = os.path.join(self.files_path, 'ssh_key')
        self.branches_path = os.path.join(self.files_path, 'branches.json')
        self.config = configuration_helper.DeployvConfig(deploy_config=self.config_path)
        self.shell = spur.LocalShell()
        with open(self.ssh_path) as ssh:
            self.ssh_key = base64.b64encode(ssh.read().encode()).decode()

    def test_copy_list_dicts(self):
        ''' Test copy_list_dicts method to copy empty dictionaries and
        dictionaries of different lengths and make sure they are copied correctly
        '''
        lines = [{'test': 1, 'default': 'test'},
                 {'test': 2, 'default': '', 'values': {}},
                 {}]
        copy_lines = utils.copy_list_dicts(lines)
        self.assertEqual(copy_lines, lines)

    def test_setup_deployv_logger_with_logfile(self):
        '''Test setup_deployv_logger passing a file to the logfile parameter
        and verify that the log file is created, the log level is the one specified
        and the logger is created.
        '''
        logger = utils.setup_deployv_logger('logger_test', logging.DEBUG, 'logfile')
        self.assertIsInstance(logger, logging.Logger)
        self.assertEqual(logger.getEffectiveLevel(), 10)
        self.assertTrue(os.path.isfile('logfile'))
        utils.clean_files('logfile')

    def test_config_deploy_logger_without_logfile(self):
        '''Test setup_deployv_logger without a logfile and check if the logger
        is created and the log level is correct.
        '''
        logger = utils.setup_deployv_logger('logger_test', logging.WARNING)
        self.assertIsInstance(logger, logging.Logger)
        self.assertEqual(logger.getEffectiveLevel(), 30)

    def test_is_iterable(self):
        ''' Test is_iterable method using a list, a dictionary, a tuple and an empty list
        and make sure if they are iterable
        '''
        iterable_list = utils.is_iterable(['a', 'b', 'c'])
        iterable_dict = utils.is_iterable({"key": "value", "key2": "value2"})
        iterable_tuple = utils.is_iterable((1,))
        iterable_empty = utils.is_iterable([])
        self.assertTrue(iterable_list)
        self.assertTrue(iterable_dict)
        self.assertTrue(iterable_tuple)
        self.assertTrue(iterable_empty)

    def test_not_iterable(self):
        ''' Test is_iterable method using a string and make sure it is not iterable
        '''
        not_iterable = utils.is_iterable('test')
        self.assertFalse(not_iterable)

    def test_merge_config(self):
        ''' Merge the ssh_key and the branches.json files located in tests/files/
        into the config.json file and verify that the result of the merge is a dict,
        that is not empty and the ssh_key and repositories keys of the dict are the same as
        the ssh_key and branches.json files respectively
        '''
        branches = json_helper.load_json(self.branches_path)
        merged_json = utils.merge_config(self.config_path, self.ssh_path, self.branches_path)
        self.assertIsInstance(merged_json, dict)
        self.assertTrue(merged_json)
        self.assertEqual(branches, merged_json.get('instance').get('repositories'))
        self.assertEqual(merged_json.get('instance').get('ssh_key'), self.ssh_key)

    def test_merge_config_with_instance_type_production(self):
        ''' Merge the ssh_key and the branches.json files located in tests/files/
        into the config.json file but with instance_type != test or development and verify
        that the result of the merge is a dict, that is not empty and the ssh_key and
        repositories keys of the dict are the same as the ssh_key and branches.json files
        respectively
        '''
        branches = json_helper.load_json(self.branches_path)
        self.config.instance_config.update({'instance_type': 'production'})
        json_helper.save_json(self.config._deploy_config, 'config.json')
        merged_json = utils.merge_config('config.json', self.ssh_path, self.branches_path)
        self.assertIsInstance(merged_json, dict)
        self.assertTrue(merged_json)
        self.assertEqual(branches, merged_json.get('instance').get('repositories'))
        self.assertEqual(merged_json.get('instance').get('ssh_key'), self.ssh_key)
        utils.clean_files('config.json')

    def test_merge_config_without_oca(self):
        ''' Merge the the ssh_key and the branches.json files located in tests/files
        into the config.json file without the oca repository and verify that the result of
        the merge is a dict, that is not empty and the ssh_key and repositories keys of the
        dict are the same as the ssh_key and branches.json files respectively
        '''
        branches = [{
            "branch": "master",
            "commit": "",
            "depth": 1,
            "is_dirty": False,
            "name": "deploy-templates",
            "path": "extra_addons/deploy-templates",
            "repo_url": {
                "origin": "git@github.com:Vauxoo/deploy-templates.git"
            },
            "type": "git"
        }]
        branches_file = json_helper.save_json(branches, 'branches.json')
        merged_json = utils.merge_config(self.config_path, self.ssh_path, branches_file)
        self.assertIsInstance(merged_json, dict)
        self.assertTrue(merged_json)
        self.assertIn(branches[0], merged_json.get('instance').get('repositories'))
        self.assertEqual(merged_json.get('instance').get('ssh_key'), self.ssh_key)
        utils.clean_files(['branches.json'])

    def test_list_backups(self):
        ''' Creates a directory and three files with different dates in order to test
        the list_backups method and make sure it returns a list with the names of the
        three files sorted from the latest to the oldest
        '''
        backup_list = ['test_20151010', 'test_20151011', 'test_20151012']
        os.makedirs('test_dir')
        for backup in backup_list:
            cmd = 'touch test_dir/{name}'.format(name=backup)
            self.shell.run(shlex.split(cmd))
        listed_backups = utils.list_backups('test_dir', 'test')
        self.assertTrue(listed_backups)
        self.assertEqual(listed_backups, backup_list[::-1])
        utils.clean_files('test_dir')

    def test_clean_files_file(self):
        ''' Creates an empty file, erase it using clean_files method
        and make sure it does not exist anymore
        '''
        self.shell.run(shlex.split('touch test_delete'))
        utils.clean_files('test_delete')
        self.assertFalse(os.path.exists('test_delete'))

    @patch('shutil.rmtree')
    def test_clean_files_root(self, mocked_class):
        ''' Tries to erase the root directory using clean_files method
        and make sure it still exists
        '''
        mc = mocked_class.return_value
        mc.rmtree.return_value = True
        utils.clean_files(['/'])
        self.assertTrue(not mocked_class.called)

    def test_clean_files_directory(self):
        ''' Creates an empty directory, erase it using clean_files method
        and make sure it does not exist anymore
        '''
        os.makedirs('tests/tobedeleted')
        utils.clean_files('tests/tobedeleted')
        self.assertFalse(os.path.exists('tests/tobedeleted'))

    def test_resume_log(self):
        ''' Loads a file containing logs and uses it as parameter for the resume_log method,
        then loads a file containing the expected result and make sure that the value
        returned the resume_log method is the same
        '''
        log_lines = json_helper.load_json(os.path.join(self.files_path, 'log_lines.json'))
        expected_logs = json_helper.load_json(os.path.join(self.files_path, 'expected_logs.json'))
        resumed_logs = utils.resume_log(log_lines)
        self.assertIsInstance(resumed_logs, dict)
        self.assertTrue(resumed_logs)
        self.assertEqual(resumed_logs, expected_logs)

    def test_get_strtime(self):
        ''' Makes sure that the date returned by the get_strtime method is
        the current date
        '''
        self.assertEqual(utils.get_strtime(),
                         datetime.now().strftime("%Y%m%d_%H%M%S"))

    def test_get_decompress_object_gz(self):
        ''' Creates a .tar.gz file, uses it with the get_decompress_method and verifies
        that the returned value is a tuple, is not empty, the first value is of type MethodType
        and the second value is r:gz
        '''

        utils.compress_files('gz_file', [self.config_path], cformat='gz')
        res = utils.get_decompress_object('gz_file.tar.gz')
        self.assertIsInstance(res, tuple)
        self.assertTrue(res)
        self.assertIsInstance(res[0], types.MethodType)
        self.assertEqual(res[1], 'r:gz')
        utils.clean_files('gz_file.tar.gz')

    def test_get_decompress_object_bz2(self):
        ''' Creates a .tar.bz2 file, uses it with the get_decompress_object method and verifies
        that the returned value is a tuple, is not empty, the first value is of type MethodType
        and the second value is r:bz2
        '''
        utils.compress_files('bz2_file', [self.config_path], cformat='bz2')
        res = utils.get_decompress_object('bz2_file.tar.bz2')
        self.assertIsInstance(res, tuple)
        self.assertTrue(res)
        self.assertIsInstance(res[0], types.MethodType)
        self.assertEqual(res[1], 'r:bz2')
        utils.clean_files('bz2_file.tar.bz2')

    def test_get_decompress_object_error(self):
        ''' Uses an uncompressed file to call the get_decompress_object method in order
        to raise a RuntimeError
        '''
        with self.assertRaises(RuntimeError):
            utils.get_decompress_object(self.config_path)

    def test_decompress_files(self):
        ''' Creates an empty database dump and creates a .tar.gz compressed file in order
        to call the decompress_files method and makes sure the files resulting of the
        decompress exist
        '''
        self.shell.run(shlex.split('touch dump.sql'))
        utils.compress_files('compressed_file', [self.config_path, 'dump.sql'],
                             cformat='gz')
        dcmp_path = os.path.join(self.main_path, 'decompress')
        decompressed_path = utils.decompress_files('compressed_file.tar.gz', dcmp_path)
        self.assertTrue(os.path.exists(decompressed_path))
        self.assertTrue(os.path.isfile(os.path.join(decompressed_path, 'config.json')))
        self.assertTrue(os.path.isfile(os.path.join(decompressed_path, 'dump.sql')))
        utils.clean_files(['compressed_file.tar.gz', dcmp_path, 'dump.sql'])

    def test_odoo2postgres(self):
        ''' Gets the instance config from the config.json and calls the odoo2postgres method
        to convert the configuration dict into a postgres configuration dict and makes sure that
        the values of the postgres configuration dict are the same as the values in the
        odoo configuration dict
        '''
        odoo_config = self.config.instance_config.get('config')
        odoo_config.update({'db_host': '172.17.0.1'})
        postgres_config = utils.odoo2postgres(odoo_config)
        self.assertIsInstance(postgres_config, dict)
        self.assertTrue(postgres_config)
        self.assertEqual(odoo_config['db_port'], postgres_config['port'])
        self.assertEqual(odoo_config['db_password'], postgres_config['password'])
        self.assertEqual(odoo_config['db_user'], postgres_config['user'])
        self.assertEqual(odoo_config['db_name'], postgres_config['dbname'])
        self.assertEqual(odoo_config['db_host'], postgres_config['host'])

    def test_generate_dbname_without_backup(self):
        ''' Generates a database name using the configuration from config.json
        with the generate_dbname method without specifying a backup
        and makes sure it is correctly generated
        '''
        db_name = utils.generate_dbname(self.config)
        self.assertEqual(db_name, '{tid}_{cid}_{time}'.format(
            cid=self.config.instance_config['customer_id'],
            tid=self.config.instance_config['task_id'],
            time=datetime.now().strftime("%Y%m%d_%H%M%S")))

    def test_generate_dbname_with_backup(self):
        ''' Generates a database name using the configuration from config.json
        with the generate_dbname method specifying a backup and makes sure
        it is correctly generated
        '''
        db_name = utils.generate_dbname(self.config, 'customer80_20151010_123456')
        self.assertEqual(db_name, '{tid}_{cid}_{time}'.format(
            cid=self.config.instance_config['customer_id'],
            tid=self.config.instance_config['task_id'], time='20151010_123456'))

    def test_generate_dbname_with_backup_without_date(self):
        ''' Generates a database name using the configuration from config.json
        with the generate_dbname method specifying a backup without date and
        makes sure it is correctly generated
        '''
        db_name = utils.generate_dbname(self.config, 'backup')
        self.assertEqual(db_name, '%s_%s_%s' % (
            self.config.instance_config['task_id'],
            self.config.instance_config['customer_id'],
            datetime.now().strftime("%Y%m%d_%H%M%S")))

    def test_generate_backup_name_with_reason(self):
        ''' Generates a backup name with the generate_backup_name method and specifying
        a reason, then makes sure the generated name has the correct format
        '''
        res = utils.generate_backup_name('test', 'reason')
        time = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.assertEqual(res, 'test_reason_{time}'.format(time=time))

    def test_generate_backup_name_without_reason(self):
        ''' Generates a backup name with the generate_backup_name method without specifying
        a reason, then makes sure the generated name has the correct format
        '''
        res = utils.generate_backup_name('test')
        time = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.assertEqual(res, 'test_{time}'.format(time=time))

    def test_decode_b64_file(self):
        ''' Copies the config.json file into a base64 coded file and decodes it using
        the decode_b64_file method, then verifies that the decoded result is the
        same as the original file
        '''
        cmd = 'openssl base64 -in %s -out config_base64' % (self.config_path)
        self.shell.run(shlex.split(cmd))
        utils.decode_b64_file('config_base64', 'decoded_config.json')
        self.assertTrue(os.path.isfile('decoded_config.json'))
        original = open(self.config_path)
        decoded = open('decoded_config.json')
        self.assertEqual(decoded.read(), original.read())
        utils.clean_files(['decoded_config.json', 'config_base64'])

    def test_compress_files_bz2(self):
        ''' Creates a .tar.bz2 compressed file into the tests folder and
        makes sure the compressed file exists
        '''
        compressed_bz2 = utils.compress_files('bz2_file', [self.config_path], dest_folder='tests')
        self.assertEqual(compressed_bz2, 'tests/bz2_file.tar.bz2')
        self.assertTrue(os.path.isfile(compressed_bz2))
        utils.clean_files(compressed_bz2)

    def test_compress_files_gz(self):
        ''' Creates a .tar.gz compressed file specifying the files to add as tuples into
        the current folder and makes sure the compressed file exists
        '''
        compressed_gz = utils.compress_files(
            'gz_file', [(self.files_path, self.config_path)], cformat='gz')
        self.assertEqual(compressed_gz, './gz_file.tar.gz')
        self.assertTrue(os.path.isfile(compressed_gz))
        utils.clean_files(compressed_gz)

    def test_compress_files_error(self):
        ''' Tries to create a compressed file using an unknown format in order to
        raise a RuntimeError
        '''
        with self.assertRaises(RuntimeError):
            utils.compress_files('foo_file', [self.config_path], cformat='foo')

    def test_generate_attachment(self):
        ''' Generates a b64 encoded string using the content of the config.json file
        with the method generate attachment and then makes sure it can be decoded
        using base64
        '''
        res = utils.generate_attachment(self.config_path)
        self.assertTrue(res)

    def test_clean_string(self):
        ''' Passes a string with all invalid chars found so far and expect them not to be
        in the string
        '''
        res = utils.clean_string('master-t#123_and$_with12#abc-dev$')
        self.assertNotRegex(res, r"[\.#\$]")

    def test_validate_external_file(self):
        ''' Verifies if a small plain text file, a big plain text file,
            and a wrong json are valid
        '''
        small_file = utils.validate_external_file(os.path.join(self.files_path, 'branches.json'))
        self.assertTrue(small_file)
        tar_file = utils.validate_external_file(os.path.join(self.files_path, 'wrong_json.json'))
        self.assertFalse(tar_file)
        with mock.patch('os.path.getsize', return_value=600000):
            big_file = utils.validate_external_file('deployv')
            self.assertFalse(big_file)

    def test_merge_dicts(self):
        ''' Passes two dictionaries to the merge_dicts method and makes sure that the
            first dictionary is updated with the second one.
        '''
        first_dict = {
            'instance': {
                'config': {
                    'test1': 1,
                    'test2': 2
                },
                'list': [1, 2, 3]
            }
        }
        second_dict = {
            'instance': {
                'config': {
                    'test2': 3
                },
                'list': [4, 5, 6]
            },
            'container': 'something'
        }
        expected_dict = {
            'instance': {
                'config': {
                    'test1': 1,
                    'test2': 3
                },
                'list': [4, 5, 6]
            },
            'container': 'something'
        }
        res = utils.merge_dicts(first_dict, second_dict)
        self.assertEqual(res, expected_dict)

    def test_random_string(self):
        ''' Calls the random_string method with a specific length and makes sure that
            the result is a string with the same length
        '''
        res = utils.random_string(5)
        self.assertIsInstance(res, string_types)
        self.assertEqual(len(res), 5)

    def test_clone_repos_fis198(self):
        with self.assertRaises(errors.NoSuchBranch):
            utils.clone_repo('https://github.com/Vauxoo/deploy-templates.git', '8.0', '/tmp/a')

    def test_parse_url(self):

        test_cases = [
            {
                'url': 'sftp://files.vauxoo.com/home/asd80',
                'res': {
                    'folder': 'home/asd80',
                    'protocol': 'sftp',
                    'port': None,
                    'domain': 'files.vauxoo.com',
                    'user': None
                }
            },
            {
                'url': 'sftp://downloads@files.vauxoo.com/home/asd80',
                'res': {
                    'folder': 'home/asd80',
                    'protocol': 'sftp',
                    'port': None,
                    'domain': 'files.vauxoo.com',
                    'user': 'downloads'
                }
            },
            {
                'url': 'sftp://downloads@ns1111.ip-111-11-00.bla/asd100',
                'res': {
                    'folder': 'asd100',
                    'protocol': 'sftp',
                    'port': None,
                    'domain': 'ns1111.ip-111-11-00.bla',
                    'user': 'downloads'
                }
            }
        ]

        for test_case in test_cases:
            self.assertDictEqual(test_case.get('res'), utils.parse_url(test_case.get('url')))

    def test_byte_converter(self):
        cases = [
            ('1KB', 'B', False, '1024.00B'),
            ('1ME', 'B', False, False),
            ('1MB', 'KP', False, False),
            ('1024B', 'KB', False, '1.00KB'),
            ('1536B', 'KB', False, '1.50KB'),
            ('1.5GB', 'MB', True, 1536),
            ('512MB', 'GB', True, 0.5),
            ('123TB', 'TB', False, '123.00TB'),
            ('123TB', 'TB', True, 123),
            ('1024  gb', 'tb', False, '1.00TB'),
            ('1B', 'B', False, '1.00B'),
        ]
        for case in cases:
            res = utils.byte_converter(case[0], to_unit=case[1], return_float=case[2])
            self.assertEqual(case[3], res)

    def test_find_files_01(self):
        """Test for the find_files method when it doesn't found the file.
        """
        res = utils.find_files('/tmp', 'asd123')
        self.assertListEqual(res, [])

    def test_find_files_02(self):
        """Test for the find_files method when it found the file.
        """
        tmp_path = mkdtemp(prefix='deployv_')
        path_file = os.path.join(tmp_path, 'test')
        with open(path_file, 'w') as w_file:
            w_file.write('write file')
        res = utils.find_files(tmp_path, 'test')
        self.assertTrue(res)
        self.assertEqual(res[0], path_file)
        utils.clean_files(tmp_path)

    def test_compare_repositories_01(self):
        """Test for the compare_repositories method when it return the repositores that have diff
        or not exist in the repositories to compared.
        """
        same = {'name': 'same', 'path': 'same', 'commit': '123'}
        repos = [{'name': 'test', 'path': 'test', 'commit': '123'}, same]
        new_repo = {'name': 'new', 'path': 'new', 'commit': '654'}
        diff_repo = {'name': 'test', 'path': 'test', 'commit': '456'}
        res = utils.compare_repositories(repos, [diff_repo, new_repo, same])
        self.assertTrue(res)
        self.assertIn(new_repo, res)
        self.assertIn(diff_repo, res)

    def test_compare_repositories_02(self):
        """Test for the compare_repositories method when it doesn't found diff between repositories.
        """
        repo = {'name': 'same', 'path': 'same', 'commit': '123'}
        res = utils.compare_repositories([repo], [repo])
        self.assertFalse(res)

    def test_add_repo_01(self):
        """Test for the `add_repo` method when add a new repo to the repositories in the config.
        """
        repo = {'branch': '8.0', 'name': 'name', 'path': 'path/name', 'commit': '', 'depth': 1,
                'repo_url': {'origin': 'repo_url'}}
        config = {'instance': {'repositories': [repo]}}
        utils.add_repo('8.0', 'test', 'path/test', 'url', config=config)
        self.assertEqual(len(config['instance']['repositories']), 2)
        self.assertIn(repo, config['instance']['repositories'])

    def test_add_repo_02(self):
        """Test for the `add_repo` method when add the new repo and only the new repo to the config.
        """
        repo = {'branch': '8.0', 'name': 'name', 'path': 'path/name', 'commit': '', 'depth': 1,
                'repo_url': {'origin': 'repo_url'}}
        config = {'instance': {'repositories': [repo]}}
        utils.add_repo('8.0', 'test', 'path/test', 'url', config=config, overwrite_repos=True)
        self.assertEqual(len(config['instance']['repositories']), 1)
        self.assertNotIn(repo, config['instance']['repositories'])

    def test_parse_repo_url(self):
        """Test for the parse_repo_url method.
        """
        # Test repo with https
        repo = 'https://github.com/test/test80.git'
        res = utils.parse_repo_url(repo)
        self.assertTrue(res)
        self.assertEqual(res['protocol'], 'https://')
        self.assertEqual(res['domain'], 'github.com')
        self.assertEqual(res['repo'], 'test/test80')
        self.assertEqual(res['namespace'], 'test')
        self.assertEqual(res['repo_name'], 'test80')
        # Test repo with ssh
        repo = 'git@git.vauxoo.com:test/test80.git'
        res = utils.parse_repo_url(repo)
        self.assertTrue(res)
        self.assertEqual(res['protocol'], 'https://')
        self.assertEqual(res['domain'], 'git.vauxoo.com')
        self.assertEqual(res['repo'], 'test/test80')
        self.assertEqual(res['namespace'], 'test')
        self.assertEqual(res['repo_name'], 'test80')
        # Test repo without .git
        repo = 'git@git.vauxoo.com:test/test80'
        res = utils.parse_repo_url(repo)
        self.assertTrue(res)
        self.assertEqual(res['protocol'], 'https://')
        self.assertEqual(res['domain'], 'git.vauxoo.com')
        self.assertEqual(res['repo'], 'test/test80')
        self.assertEqual(res['namespace'], 'test')
        self.assertEqual(res['repo_name'], 'test80')
        res = utils.parse_repo_url('test')
        self.assertFalse(res)
        self.assertIsInstance(res, dict)

    @mock.patch('deployv.helpers.utils.open', create=True)
    def test_read_lines(self, mock_open):
        cases = [
            ('     \n \n\n   ', []),
            ('     \n line 2 \n   \n  line 3\n\n    \n', ['line 2', 'line 3']),
        ]
        mock_open.side_effect = [mock.mock_open(read_data=c[0]).return_value for c in cases]
        for c in cases:
            res = utils.read_lines('somefile.txt')
            self.assertListEqual(res, c[1])
