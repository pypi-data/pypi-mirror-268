# coding: utf-8
from unittest import TestCase
import psycopg2
import spur
import os
from deployv.base import errors
from deployv.base.postgresv import PostgresShell
from deployv.base.postgresv import PostgresConnector
from deployv.helpers import utils, json_helper


class TestPostgresV(TestCase):

    @classmethod
    def setUp(cls):
        cls.conf = {
            "user": "postgres",
            "isolation_level": True
        }
        cls.wrong_config = {'user': 'wrong',
                            'password': 'wrong',
                            'host': '172.17.42.1',
                            'port': 5432, 'dbname': None}
        cnf_path = os.path.join(os.path.dirname(__file__), 'files/config.json')
        json_file = json_helper.load_json(cnf_path)
        instance_config = json_file.get('instance').get('config')
        mapping = {
            'user': ['db_user', 'DB_USER'],
            'host': ['db_host', 'DB_HOST'],
            'port': ['db_port', 'DB_PORT'],
            'password': ['db_password', 'DB_PASSWORD'],
        }
        for psql_key, psql_value in mapping.items():
            for odoo_key, odoo_value in instance_config.items():
                if odoo_key in psql_value:
                    cls.conf.update({psql_key: odoo_value})
        cls.postgres_shell = PostgresShell(cls.conf)
        cls.connector = PostgresConnector(cls.conf)
        cls.shell = spur.LocalShell()

    def test_init_exception(self):
        ''' Use wrong configuration to check if the try-except block in the
        PostgresConnector init method works
        '''
        self.wrong_config.update({'dbname': None})
        with self.assertRaises(psycopg2.OperationalError):
            PostgresConnector(self.wrong_config)

    def test_create_db(self):
        ''' Creates a db using the PostgresShel create method and
        makes sure the db is created with the name specified to the method
        and check that the db exists.
        '''
        db_name = self.postgres_shell.create('test_db_create')
        self.assertEqual(db_name, 'test_db_create')
        res = self.shell.run(["sh", "-c", "psql -l | grep test_db_create | wc -l"])
        self.assertEqual(int(res.output.decode().strip('\n')), 1)
        self.postgres_shell.drop('test_db_create')

    def test_create_db_exception(self):
        ''' Try to create a database using wrong configuration in order
        to test if the try-except block of the create method works
        '''
        pg_shell = PostgresShell(self.wrong_config)
        with self.assertRaises(psycopg2.OperationalError):
            pg_shell.create('test_create_exception')

    def test_dump_db(self):
        ''' Creates a database and dumps it in tests/, then verifies the
        .sql file with the database dump exists
        '''
        db_name = self.postgres_shell.create('test_db_dump')
        dump = self.postgres_shell.dump(db_name, 'tests/dump.sql')
        self.assertEqual(dump, 'tests/dump.sql')
        self.assertTrue(os.path.isfile('tests/dump.sql'))
        utils.clean_files('dump.sql')
        self.postgres_shell.drop('test_db_dump')

    def test_dump_db_exceptions(self):
        ''' Tries to do a dump of an inexistent database and create a dump
        file as a directory in order to tests the exceptions in the dump method
        '''
        with self.assertRaises(errors.DumpError):
            self.postgres_shell.dump('wrong_db', 'db.sql')
        db_name = self.postgres_shell.create('test_exception')
        with self.assertRaises(errors.DumpError):
            self.postgres_shell.dump(db_name, 'tests/')
        self.postgres_shell.drop('test_exception')

    def test_list_db(self):
        ''' Creates a database and then get the databases using the
        list_databases method, then makes sure the created database
        is listed in the result returned by the method
        '''
        self.postgres_shell.create('test_db_list')
        result = self.postgres_shell.list_databases()
        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, dict)
        expected = {
            'owner': '{user}'.format(user=self.conf.get('user')),
            'name': 'test_db_list',
            'encoding': 'UTF8'
        }
        self.assertIn(expected, result)
        self.postgres_shell.drop('test_db_list')

    def test_drop_db(self):
        ''' Creates a database to be deleted usign drop method and make sure
        the result is True, then try to do a search of the database name
        in the list of databases and then count the words of the  result which
        should be 0.
        '''
        self.postgres_shell.create('test_db_drop')
        drop_db = self.postgres_shell.drop('test_db_drop')
        self.assertTrue(drop_db)
        res = self.shell.run(["sh", "-c", "psql -l | grep test_db_drop | wc -l"])
        self.assertEqual(int(res.output.decode().strip('\n')), 0)
        drop_db = self.postgres_shell.drop('fake_db')
        self.assertTrue(drop_db)

    def test_drop_db_exception(self):
        ''' Tries to drop a database using wrong configuration in order
        to test the try-except block in the drop method
        '''
        pg_shell = PostgresShell(self.wrong_config)
        with self.assertRaises(psycopg2.OperationalError):
            pg_shell.drop('test_db_list')
        wrong_db = self.postgres_shell.drop('wrong_database')
        self.assertTrue(wrong_db)

    def test_restore_db(self):
        ''' Creates a fake dump and test if the restore method works by creating
        a new database using that dump and check that the database is created
        '''
        self.postgres_shell.create('restored_db')
        restore = self.postgres_shell.restore('restored_db', 'tests/dump.sql')
        self.assertTrue(restore)
        res = self.shell.run(["sh", "-c", "psql -l | grep restored_db | wc -l"])
        self.assertEqual(int(res.output.decode().strip('\n')), 1)
        self.postgres_shell.drop('restored_db')
        utils.clean_files('tests/dump.sql')

    def test_restore_db_exceptions(self):
        ''' Tries to restore a database using wrong configuration in order
        to test the try-except block in the restore method
        '''
        with self.assertRaises(psycopg2.OperationalError):
            self.postgres_shell.restore('test_db', 'tests/')

    def test_insert(self):
        ''' Uses the execute method to create a table and insert data in it
        '''
        self.postgres_shell.create('test_db_execute')
        self.conf.update({"dbname": 'test_db_execute'})
        connector = PostgresConnector(self.conf)
        sql_str = "CREATE TABLE test_table (ID INT, NAME TEXT, AGE INT);"
        create = connector.execute(sql_str)
        self.assertTrue(create)
        sql_str = "INSERT INTO test_table (ID, NAME, AGE) VALUES (%s, %s, %s);"
        args = (12345, "test", 23)
        insert = connector.execute(sql_str, args)
        self.assertTrue(insert)

    def test_select(self):
        ''' Uses the execute method to do a select and makes sure the table
        created in the test_insert does exist
        '''
        self.conf.update({"dbname": 'test_db_execute'})
        connector = PostgresConnector(self.conf)
        sql_str = ('SELECT table_name FROM information_schema.tables'
                   ' WHERE table_schema=\'public\' AND table_type=\'BASE TABLE\';')
        result = connector.execute(sql_str)
        self.assertEqual(result, [{'table_name': 'test_table'}])

    def test_update(self):
        ''' Uses the exec method to do an update of the data in the
        table created in the test_insert
        '''
        self.conf.update({"dbname": 'test_db_execute'})
        with PostgresConnector(self.conf) as connector:
            sql_str = "UPDATE test_table SET AGE=26 WHERE ID=12345"
            result = connector.execute(sql_str)
            self.assertTrue(result)
        self.postgres_shell.drop('test_db_execute')

    def test_correct_config(self):
        ''' Test if the check_config method returns true when
        the config is correct
        '''
        result = self.connector.check_config()
        self.assertTrue(result)

    def test_check_config_exception(self):
        ''' Closes connection with postgres and calls the check_config method
        in order to test if the try-except block works
        '''
        self.conf.update({'dbname': 'postgres'})
        connector = PostgresConnector(self.conf)
        connector.disconnect()
        res = connector.check_config()
        self.assertFalse(res)

    def test_disconnect(self):
        ''' Disconnects from postgres and then tries to do a query to the database
        and expects an error in order to make sure the database connection
        was successfully closed
        '''
        self.conf.update({'dbname': 'postgres'})
        connector = PostgresConnector(self.conf)
        connector.disconnect()
        sql_str = ('SELECT table_name FROM information_schema.tables'
                   ' WHERE table_schema=\'public\' AND table_type=\'BASE TABLE\';')
        with self.assertRaises(psycopg2.InterfaceError):
            connector.execute(sql_str)

    def test_execute_exception(self):
        ''' Tries to do a wrong query to the database in order to test
        the try-except block in execute method
        '''
        with self.assertRaises(psycopg2.ProgrammingError):
            self.connector.execute('wrong query;')
