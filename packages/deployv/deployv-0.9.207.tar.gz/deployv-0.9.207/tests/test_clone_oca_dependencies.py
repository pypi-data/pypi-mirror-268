# coding: utf-8
from unittest import TestCase
import os
from deployv.helpers import clone_oca_dependencies, utils
from mock import patch
import spur
import shlex


class Test_clone_oca_dependencies(TestCase):

    def setUp(self):
        self.path = os.path.join(os.path.dirname(__file__), 'files')
        self.oca_dependencies = os.path.join(self.path, 'oca_dependencies.txt')

    def tearDown(self):
        utils.clean_files(os.path.join(self.path, 'foo'))
        utils.clean_files(os.path.join(self.path, 'pre_process.json'))

    def test_01_parse_depfile(self):
        """
        Test parse_depfile methods parse file text plain oca_dependencies.txt
        to send file test for verify and get context and return dict
        """
        oca = open(self.oca_dependencies, 'r')
        deps = clone_oca_dependencies.parse_depfile(oca, '8.0')
        self.assertTrue(deps)
        self.assertIsInstance(deps, list)
        self.assertEqual(len(deps), 6)
        for dep in deps:
            self.assertIsInstance(dep, tuple)
            self.assertEqual(len(dep), 4)
        self.assertIn(('odoo', 'http://another.url/', 'anotherbranch', False), deps)
        self.assertIn(('bundle', 'http://doe.com/joe', 'master', False), deps)
        self.assertIn(('addon', 'http://myurl.com/foo', 'branch', False), deps)
        self.assertIn(('bar', 'http://bar.foo/jhon', '8.0', False), deps)
        self.assertIn(('repo_name', 'git@gilab.com:org/repo_name', '12.0', 'C0mm1t5h4'), deps)
        self.assertEqual('foo', deps[1][0])

    @patch('deployv.helpers.clone_oca_dependencies.load_branches')
    def test_02_git_checkout(self, mocked_class):
        """
        Test git_checkout methods, this method validate if do not
        exists repository and download repository
        of github to test method the contents of a text
        file is sent with the requirements
        is validated if it returns an address
        """
        mocked_class.return_value = False
        oca = open(self.oca_dependencies, 'r')
        deps = clone_oca_dependencies.parse_depfile(oca, '8.0')
        for depname, url, branch, commit in deps:
            checkout = clone_oca_dependencies.\
                git_checkout('/tmp', depname, url, branch, commit, '/tmp')
            self.assertIsInstance(checkout[1], str)
            self.assertIn(depname, checkout[1])
            self.assertEqual(os.path.join('/tmp', depname), checkout[1])
        self.assertTrue(mocked_class.called)

    @patch('deployv.helpers.clone_oca_dependencies.load_branches')
    def test_03_get_dep_filename(self, mocked_class):
        """
        Test get_dep_filename methods, this methods passing
        dirs with file oca_dependencies.txt
        and valdate returns list
        """
        repo_test = os.path.join(self.path, 'foo')
        os.mkdir(repo_test)
        mocked_class.return_value = False
        oca_dependencies = clone_oca_dependencies.\
            get_dep_filename(self.path, self.path,
                             'oca_dependencies.txt', '8.0', '/tmp')
        self.assertIsInstance(oca_dependencies[1], list)
        self.assertIn(self.oca_dependencies, oca_dependencies[1])

    @patch('deployv.helpers.clone_oca_dependencies.load_branches')
    def test_04_run(self, mocked_class):
        """
        Test run methods, this methods passing
        dirs with file oca_dependencies.txt
        """
        mocked_class.return_value = False
        res = clone_oca_dependencies.run(self.path, self.path, '8.0', '/tmp')
        self.assertTrue(res[0])
        self.assertIsInstance(res[1], list)

    def test_05_fix198(self):
        """
        Test to check if issue https://git.vauxoo.com/vauxoo/orchest/issues/198
        was fixed properly, an exception should be raised
        """
        result = clone_oca_dependencies.\
            git_checkout('/tmp', 'deploy-templates',
                         'https://github.com/Vauxoo/deploy-templates.git',
                         '8.0', tmp_folder='/tmp')
        self.assertFalse(result[0])
        self.assertIn('fatal: Remote branch 8.0 not found', result[1])

    @patch('deployv.helpers.clone_oca_dependencies.load_branches')
    def test_06_execute_command_line(self, mocked_class):
        mocked_class.return_value = False
        shell = spur.LocalShell()
        file_name = clone_oca_dependencies.__file__.replace("pyc", 'py')
        cmd = "python3 {file_py} {path} {path} 8.0 {path}".format(
            file_py=file_name, path=self.path)
        res = shell.run(shlex.split(cmd))
        self.assertEqual(res.return_code, 0)
