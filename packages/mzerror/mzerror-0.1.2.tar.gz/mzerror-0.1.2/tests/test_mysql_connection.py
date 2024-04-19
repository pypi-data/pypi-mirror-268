import unittest
from dotenv import find_dotenv, load_dotenv
import os
from mzerror import MySQLConnection

env_file = find_dotenv()
load_dotenv()

DB_HOST = os.environ["DB_HOST"]
DB_USER = os.environ["DB_USER"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_NAME = os.environ["DB_NAME"]


class TestMySQLConnection(unittest.TestCase):

    def setUp(self):
        self.connection = MySQLConnection(
            host=DB_HOST,
            username=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )

    def test_select_all(self):
        table_name = "errors_main"
        columns = ["id"]
        values = [0]
        result = self.connection.select(table_name=table_name, columns=columns, values=values)
        self.assertEqual(len(result), 1)

    def test_select(self):
        table_name = "errors_main"
        select_columns = ["id", "error_name"]
        columns = ["id"]
        values = [0]
        result = self.connection.select(table_name=table_name, columns=columns, values=values, select_columns=select_columns)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], {"id": 0, "error_name": "UNKNOWN_ERROR"})

