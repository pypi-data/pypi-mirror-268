import unittest
from tests.test_error_handler import TestErrorHandler
from tests.test_mysql_connection import TestMySQLConnection


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestErrorHandler))
    test_suite.addTest(unittest.makeSuite(TestMySQLConnection))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
