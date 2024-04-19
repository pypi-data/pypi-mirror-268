# coding: utf-8
import os
import tempfile
from unittest import TestCase

from deployv.helpers import pg_anon


class TestPostgresV(TestCase):

    def setUp(self):
        self.tmp_file = os.path.join(tempfile.gettempdir(), "operations.csv")
        with open(self.tmp_file, 'w') as fh:
            fh.write("TAbLE: res_bank\n")
            fh.write("name,alpha,10\n")
            fh.write("street,LastName\n")
            fh.write("email,Email,3\n")
            fh.write("table: res_groups\n")
            fh.write("color,DIGIT,1-16\n")
            fh.write("\n")
            fh.write("comment,ConstantStr,Comment 1\n")
            fh.write("\n")
            fh.write("table: res_partner\n")
            fh.write("vat,PatteRn,V\A111AAAZZ1\n")   # noqa: W605
            fh.write("\n")
            fh.write("city,City\n")
            fh.write("email,Email\n")
            fh.write("color,constantnum,3\n")
            fh.write("\n")
            fh.write("\n")
            fh.write("phone,Pattern,(+52)111-1111111\n")
            fh.write("company_name,Name\n")

    def test_01_01_get_args_pattern(self):
        code_pattern = "DE-111-AA"
        expected_result = ("DE-%s-%s", "[1, 3], [2, 2]")
        res = pg_anon.get_args_pattern(code_pattern)
        self.assertTupleEqual(res, expected_result)

    def test_01_02_get_args_pattern(self):
        code_pattern = "V\A111FYAAAZZ1"   # noqa: W605
        expected_result = ("VA%sFY%s%s%s", "[1, 3], [2, 3], [3, 2], [1, 1]")
        res = pg_anon.get_args_pattern(code_pattern)
        self.assertTupleEqual(res, expected_result)

    def test_01_03_get_args_pattern(self):
        code_pattern = "C111-B\Z11-EFZZ"   # noqa: W605
        expected_result = ("C%s-BZ%s-EF%s", "[1, 3], [1, 2], [3, 2]")
        res = pg_anon.get_args_pattern(code_pattern)
        self.assertTupleEqual(res, expected_result)

    def test_02_01_get_masking_function(self):
        """Test for field_type ConstantNum"""
        expected_result = "SECURITY LABEL FOR anon ON COLUMN res_users.status " \
                          "IS 'MASKED WITH VALUE 3'; "
        res = pg_anon.get_masking_function("res_users", "status", "ConsTantnUm", "3")
        self.assertEqual(res, expected_result)

    def test_02_02_get_masking_function(self):
        """Test for field_type ConstantNum without argument"""
        res = pg_anon.get_masking_function("res_users", "status", "ConsTantnUm", None)
        self.assertEqual(res, '')

    def test_02_03_get_masking_function(self):
        """Test for field_type ConstantStr"""
        expected_result = "SECURITY LABEL FOR anon ON COLUMN res_users.title " \
                          "IS 'MASKED WITH VALUE ''Mr.'' '; "
        res = pg_anon.get_masking_function("res_users", "title", "conStanTStR", "Mr.")
        self.assertEqual(res, expected_result)

    def test_02_04_get_masking_function(self):
        """Test for field_type ConstantStr without argument"""
        res = pg_anon.get_masking_function("res_users", "title", "conStanTStR", None)
        self.assertEqual(res, '')

    def test_02_05_get_masking_function(self):
        """Test for field_type Digit with specific length"""
        expected_result = "SECURITY LABEL FOR anon ON COLUMN account_account.prefix " \
                          "IS 'MASKED WITH FUNCTION anon.random_int_between(100, 999)'; "
        res = pg_anon.get_masking_function("account_account", "prefix", "diGit", "3")
        self.assertEqual(res, expected_result)

    def test_02_06_get_masking_function(self):
        """Test for field_type Digit with range length"""
        expected_result = "SECURITY LABEL FOR anon ON COLUMN sale_order.quantity " \
                          "IS 'MASKED WITH FUNCTION anon.random_int_between(1, 26)'; "
        res = pg_anon.get_masking_function("sale_order", "quantity", "digiT", "1-26")
        self.assertEqual(res, expected_result)

    def test_02_07_get_masking_function(self):
        """Test for field_type Digit without length"""
        res = pg_anon.get_masking_function("account_account", "prefix", "diGit", None)
        self.assertEqual(res, '')

    def test_02_08_get_masking_function(self):
        """Test for field_type Alpha"""
        expected_result = "SECURITY LABEL FOR anon ON COLUMN account_account.code " \
                          "IS 'MASKED WITH FUNCTION vx.random_alpha(8)'; "
        res = pg_anon.get_masking_function("account_account", "code", "alPha", "8")
        self.assertEqual(res, expected_result)

    def test_02_09_get_masking_function(self):
        """Test for field_type Alpha without length"""
        res = pg_anon.get_masking_function("account_account", "code", "alPha", None)
        self.assertEqual(res, '')

    def test_02_10_get_masking_function(self):
        """Test for field_type AlphaNumeric"""
        expected_result = "SECURITY LABEL FOR anon ON COLUMN account_account.code2 " \
                          "IS 'MASKED WITH FUNCTION anon.random_string(6)'; "
        res = pg_anon.get_masking_function("account_account", "code2", "alPhanUmeRic", "6")
        self.assertEqual(res, expected_result)

    def test_02_11_get_masking_function(self):
        """Test for field_type AlphaNumeric without length"""
        res = pg_anon.get_masking_function("account_account", "code2", "alPhanUmeRic", None)
        self.assertEqual(res, '')

    def test_02_12_get_masking_function(self):
        """Test for field_type Pattern"""
        expected_result = "SECURITY LABEL FOR anon ON COLUMN res_partner.vat " \
                          "IS 'MASKED WITH FUNCTION vx.pattern(''A%s%sT%s%s'', " \
                          "ARRAY [[1, 3], [2, 2], [3, 2], [1, 1]])'; "
        res = pg_anon.get_masking_function("res_partner", "vat",
                                           "paTteRn", "\A111AATZZ1")   # noqa: W605
        self.assertEqual(res, expected_result)

    def test_02_13_get_masking_function(self):
        """Test for field_type Pattern"""
        expected_result = \
            "SECURITY LABEL FOR anon ON COLUMN res_company.bank_account_code_prefix " \
            "IS 'MASKED WITH FUNCTION vx.pattern(''%s.%s.%s'', ARRAY [[1, 3], [1, 2], [1, 1]])'; "
        res = pg_anon.get_masking_function("res_company", "bank_account_code_prefix",
                                           "pAtTerN", "111.11.1")
        self.assertEqual(res, expected_result)

    def test_02_14_get_masking_function(self):
        """Test for field_type Pattern without argument"""
        res = pg_anon.get_masking_function("res_company", "bank_account_code_prefix",
                                           "pAtTerN", None)
        self.assertEqual(res, '')

    def test_02_15_get_masking_function(self):
        """Test for field_type FirstName with unnecessary argument"""
        expected_result = "SECURITY LABEL FOR anon ON COLUMN res_users.first_name " \
                          "IS 'MASKED WITH FUNCTION anon.fake_first_name()'; "
        res = pg_anon.get_masking_function("res_users", "first_name", "fiRstnAmE", "5")
        self.assertEqual(res, expected_result)

    def test_02_16_get_masking_function(self):
        """Test for field_type FirstName"""
        expected_result = "SECURITY LABEL FOR anon ON COLUMN res_users.first_name " \
                          "IS 'MASKED WITH FUNCTION anon.fake_first_name()'; "
        res = pg_anon.get_masking_function("res_users", "first_name", "fiRstnAmE", None)
        self.assertEqual(res, expected_result)

    def test_02_17_get_masking_function(self):
        """Test for field_type LastName with unnecessary argument"""
        expected_result = "SECURITY LABEL FOR anon ON COLUMN res_users.last_name " \
                          "IS 'MASKED WITH FUNCTION anon.fake_last_name()'; "
        res = pg_anon.get_masking_function("res_users", "last_name", "lAstNamE", "7")
        self.assertEqual(res, expected_result)

    def test_02_18_get_masking_function(self):
        """Test for field_type LastName"""
        expected_result = "SECURITY LABEL FOR anon ON COLUMN res_users.last_name " \
                          "IS 'MASKED WITH FUNCTION anon.fake_last_name()'; "
        res = pg_anon.get_masking_function("res_users", "last_name", "lAstNamE", None)
        self.assertEqual(res, expected_result)

    def test_02_19_get_masking_function(self):
        """Test for field_type Email with unnecessary argument"""
        expected_result = "SECURITY LABEL FOR anon ON COLUMN res_company.email " \
                          "IS 'MASKED WITH FUNCTION anon.fake_email()'; "
        res = pg_anon.get_masking_function("res_company", "email", "eMaIl", "6")
        self.assertEqual(res, expected_result)

    def test_02_20_get_masking_function(self):
        """Test for field_type Email"""
        expected_result = "SECURITY LABEL FOR anon ON COLUMN res_company.email " \
                          "IS 'MASKED WITH FUNCTION anon.fake_email()'; "
        res = pg_anon.get_masking_function("res_company", "email", "eMaIl", None)
        self.assertEqual(res, expected_result)

    def test_02_21_get_masking_function(self):
        """Test for field_type Country with unnecessary argument"""
        expected_result = "SECURITY LABEL FOR anon ON COLUMN res_country.name " \
                          "IS 'MASKED WITH FUNCTION anon.fake_country()'; "
        res = pg_anon.get_masking_function("res_country", "name", "coUntRy", "4")
        self.assertEqual(res, expected_result)

    def test_02_22_get_masking_function(self):
        """Test for field_type Country"""
        expected_result = "SECURITY LABEL FOR anon ON COLUMN res_country.name " \
                          "IS 'MASKED WITH FUNCTION anon.fake_country()'; "
        res = pg_anon.get_masking_function("res_country", "name", "coUntRy", None)
        self.assertEqual(res, expected_result)

    def test_02_23_get_masking_function(self):
        """Test for field_type Country with unnecessary argument"""
        expected_result = "SECURITY LABEL FOR anon ON COLUMN res_partner.city " \
                          "IS 'MASKED WITH FUNCTION anon.fake_city()'; "
        res = pg_anon.get_masking_function("res_partner", "city", "ciTy", "8")
        self.assertEqual(res, expected_result)

    def test_02_24_get_masking_function(self):
        """Test for field_type Country"""
        expected_result = "SECURITY LABEL FOR anon ON COLUMN res_partner.city " \
                          "IS 'MASKED WITH FUNCTION anon.fake_city()'; "
        res = pg_anon.get_masking_function("res_partner", "city", "ciTy", None)
        self.assertEqual(res, expected_result)

    def test_02_25_get_masking_function(self):
        """Test for field_type Company with unnecessary argument"""
        expected_result = \
            "SECURITY LABEL FOR anon ON COLUMN res_partner.commercial_company_name " \
            "IS 'MASKED WITH FUNCTION anon.fake_company()'; "
        res = pg_anon.get_masking_function("res_partner", "commercial_company_name",
                                           "coMpaNy", "3")
        self.assertEqual(res, expected_result)

    def test_02_26_get_masking_function(self):
        """Test for field_type Company"""
        expected_result = \
            "SECURITY LABEL FOR anon ON COLUMN res_partner.commercial_company_name " \
            "IS 'MASKED WITH FUNCTION anon.fake_company()'; "
        res = pg_anon.get_masking_function("res_partner", "commercial_company_name",
                                           "coMpaNy", None)
        self.assertEqual(res, expected_result)

    def test_03_01_get_queries_from_operations_file(self):
        expected_result = [
            "SECURITY LABEL FOR anon ON COLUMN res_bank.name "
            "IS 'MASKED WITH FUNCTION vx.random_alpha(10)'; "
            "SECURITY LABEL FOR anon ON COLUMN res_bank.street "
            "IS 'MASKED WITH FUNCTION anon.fake_last_name()'; "
            "SECURITY LABEL FOR anon ON COLUMN res_bank.email "
            "IS 'MASKED WITH FUNCTION anon.fake_email()'; "
            "SELECT anon.anonymize_table('res_bank');",
            "SECURITY LABEL FOR anon ON COLUMN res_groups.color "
            "IS 'MASKED WITH FUNCTION anon.random_int_between(1, 16)'; "
            "SECURITY LABEL FOR anon ON COLUMN res_groups.comment "
            "IS 'MASKED WITH VALUE ''Comment 1'' '; "
            "SELECT anon.anonymize_table('res_groups');",
            "SECURITY LABEL FOR anon ON COLUMN res_partner.vat "
            "IS 'MASKED WITH FUNCTION vx.pattern(''VA%s%s%s%s'', "
            "ARRAY [[1, 3], [2, 3], [3, 2], [1, 1]])'; "
            "SECURITY LABEL FOR anon ON COLUMN res_partner.city "
            "IS 'MASKED WITH FUNCTION anon.fake_city()'; "
            "SECURITY LABEL FOR anon ON COLUMN res_partner.email "
            "IS 'MASKED WITH FUNCTION anon.fake_email()'; "
            "SECURITY LABEL FOR anon ON COLUMN res_partner.color "
            "IS 'MASKED WITH VALUE 3'; "
            "SECURITY LABEL FOR anon ON COLUMN res_partner.phone "
            "IS 'MASKED WITH FUNCTION vx.pattern(''(+52)%s-%s'', "
            "ARRAY [[1, 3], [1, 7]])'; "
            "SECURITY LABEL FOR anon ON COLUMN res_partner.company_name "
            "IS 'MASKED WITH FUNCTION vx.random_name()'; "
            "SELECT anon.anonymize_table('res_partner');"]
        res = pg_anon.get_queries_from_operations_file(self.tmp_file)
        self.assertListEqual(res, expected_result)
