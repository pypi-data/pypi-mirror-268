# coding: utf-8
import base64
import mock
import shlex
import spur
import os
import zipfile
from unittest import TestCase
from deployv.helpers import database_helper, utils, json_helper
from deployv.base import errors, postgresv


class TestDatabaseHelper(TestCase):

    @classmethod
    def setUpClass(cls):
        cnf_path = os.path.join(os.path.dirname(__file__), 'files/config.json')
        config_file = json_helper.load_json(cnf_path)
        db_config = config_file.get('instance').get('config')
        db_config.update({'db_name': 'template1'})
        cls.db_config = utils.odoo2postgres(db_config)
        cls.copy_helper = database_helper.DatabaseHelper.get_helper(True)
        cls.backup_helper = database_helper.DatabaseHelper.get_helper(False)
        cls.shell = spur.LocalShell()

    def test_10_not_implemented_exception(self):
        ''' Test that the correct exceptions are raised when we try to
        call a helper method that has not been implemented.
        '''
        db_helper = database_helper.DatabaseHelper(self.db_config, self.db_config)
        with self.assertRaises(errors.MethodNotImplemented):
            db_helper.search_candidate()
        with self.assertRaises(errors.MethodNotImplemented):
            db_helper.create_database()

    def test_20_get_helper(self):
        ''' Test for the get_helper method that verifies if the class returned
        is the correct one.
        '''
        obj = database_helper.DatabaseHelper.get_helper(True)
        self.assertEqual(obj, database_helper.CopyDatabase)
        obj = database_helper.DatabaseHelper.get_helper(False)
        self.assertEqual(obj, database_helper.RestoreBackup)

    def test_30_copydatabase_search_candidate(self):
        ''' Test the CopyDatabase.search_candidate method to make sure
        that it returns a correct database name.
        '''
        helper = self.copy_helper(self.db_config, self.db_config)
        postgres_shell = postgresv.PostgresShell(self.db_config)
        candidate = helper.search_candidate('test30')
        self.assertFalse(candidate[0])
        postgres_shell.create('original_test30_1')
        candidate = helper.search_candidate('test30')
        self.assertTrue(candidate[0])
        self.assertEqual('original_test30_1', candidate[1])
        postgres_shell.create('original_test30_2')
        candidate = helper.search_candidate('test30')
        self.assertTrue(candidate[0])
        self.assertEqual('original_test30_2', candidate[1])

    def test_40_copydatabase_create_database(self):
        ''' Test the CopyDatabase.create_database method to make sure
        that it can create a new database by copying the one returned by
        the search_candidate method.
        '''
        helper = self.copy_helper(self.db_config, self.db_config)
        source = helper.search_candidate('test30')
        res = helper.create_database(source[1], 'test40', 'docker', 'docker')
        self.assertTrue(res[0])
        self.assertEqual('test40', res[1])
        shell = postgresv.PostgresShell(self.db_config)
        databases = shell.list_databases()
        self.assertIn({'owner': 'docker', 'name': 'test40', 'encoding': 'UTF8'},
                      databases)

    def test_50_restorebackup_check_backup_folder(self):
        ''' Test the RestoreBackup._check_backup_folder method to make sure
        that it returns the latest backup in a directory.
        '''
        helper = self.backup_helper(self.db_config, self.db_config)
        res = helper._check_backup_folder('/non/existing/backup/', 'test50')
        self.assertFalse(res[0])
        os.mkdir('backups')
        res = helper._check_backup_folder('backups', 'test50')
        self.assertFalse(res[0])
        self.shell.run(shlex.split('touch backups/test50_12345_54321.tar.bz2'))
        res = helper._check_backup_folder('backups', 'test50')
        self.assertTrue([0])
        self.assertEqual('backups/test50_12345_54321.tar.bz2', res[1])
        self.shell.run(shlex.split('touch backups/dump.sql'))
        res = helper._check_backup_folder('backups', 'test50')
        self.assertTrue([0])
        self.assertEqual('backups', res[1])
        res = helper._check_backup_folder('backups/dump.sql', 'test50')
        self.assertTrue([0])
        self.assertEqual('backups/dump.sql', res[1])

    def test_60_restorebackup_get_dump(self):
        ''' Test the RestoreBackup._get_dump method to make sure that it can
        get the correct dump.
        '''
        helper = self.backup_helper(self.db_config, self.db_config)
        res = helper._get_dump('backups')
        self.assertEqual(res, 'backups/dump.sql')
        with zipfile.ZipFile('backups/backup.zip', 'w') as bkp:
            bkp.write('backups/dump.sql')
        with open('backups/backup.zip', 'rb') as input_file,\
                open('backups/database_dump.b64', 'wb') as output_file:
            base64.encode(input_file, output_file)
        res = helper._get_dump('backups')
        self.assertEqual(res, 'backups/dump.sql')
        self.shell.run(shlex.split('touch backups/dump.sql'))
        res = helper._get_dump('backups')
        self.assertEqual(res, 'backups/dump.sql')

    def test_70_restorebackup_search_candidate(self):
        ''' Test the RestoreBackup.search_candidate to make sure that it returns
        the latest backup.
        '''
        helper = self.backup_helper(self.db_config, self.db_config)
        res = helper.search_candidate('non/existing/backup', 'test70')
        self.assertFalse(res[0])
        res = helper.search_candidate('backups', 'test70')
        self.assertTrue(res[0])
        self.assertEqual(res[1], 'backups')

    def test_80_restorebackup_create_database(self):
        ''' Test to make sure that the RestoreBackup.create_database method can
        create a new database using the backup returned by the search_candidate method
        '''
        helper = self.backup_helper(self.db_config, self.db_config)
        res = helper.create_database('backups', 'test80', 'docker', 'docker')
        self.assertTrue(res[0])
        self.assertEqual(res[1], 'test80')

    @mock.patch('deployv.helpers.database_helper.RestoreBackup._get_dump')
    def test_90_restorebackup_create_database_error(self, mock_method):
        ''' Test to make sure that the exception when we specify a wrong path is
        correctly catched.
        '''
        mock_method.return_value = False
        helper = self.backup_helper(self.db_config, self.db_config)
        res = helper.create_database('backups', 'test90', 'docker', 'docker')
        self.assertFalse(res[0])

    def test_99_clean_up(self):
        self.db_config.update({'dbname': 'template1'})
        postgres_shell = postgresv.PostgresShell(self.db_config)
        postgres_shell.drop('original_test30_1')
        postgres_shell.drop('original_test30_2')
        postgres_shell.drop('test40')
        postgres_shell.drop('test80')
        utils.clean_files('backups')
