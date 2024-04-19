import os
import unittest
from datetime import datetime, timedelta, timezone
from os.path import join

from dotenv import find_dotenv, load_dotenv
from jinja2 import Environment, FileSystemLoader

from mzerror import ErrorHandler

env_file = find_dotenv()
load_dotenv()

PROJECT_PATH = os.environ["PROJECT_PATH"]

DB_HOST = os.environ["DB_HOST"]
DB_USER = os.environ["DB_USER"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_NAME = os.environ["DB_NAME"]

RECEIVER_EMAIL = os.environ["RECEIVER_EMAIL"]
PROD_EMAIL = os.environ["PROD_EMAIL"]
SENDER_EMAIL = os.environ["SENDER_EMAIL"]
SENDGRID_API_KEY = os.environ["SENDGRID_API_KEY"]


class TestErrorHandler(unittest.TestCase):

    def setUp(self):
        self.error_handler = ErrorHandler(script_name="test", script_path="path/to/test")
        self.error_handler_no_email = ErrorHandler(script_name="test", script_path="path/to/test", is_send_email=False)
        self.error_handler_no_database = ErrorHandler(script_name="test", script_path="path/to/test", is_send_email=False)
        print(join(PROJECT_PATH, 'test', 'templates'))
        self.template_env = Environment(loader=FileSystemLoader(join(PROJECT_PATH, 'tests', 'templates')))
        self.sample_template = self.template_env.get_template("sample_template.html")

        self.error_handler.setup_connection(
            host=DB_HOST,
            username=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            error_log_table_name="errors_log",
            error_table_name="errors_main"
        )
        self.error_handler_no_email.setup_connection(
            host=DB_HOST,
            username=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            error_log_table_name="errors_log",
            error_table_name="errors_main"
        )

        self.error_handler.setup_email(
            from_email=SENDER_EMAIL,
            module=2,
            sendgrid_api_key=SENDGRID_API_KEY,
            emails_to_send=[RECEIVER_EMAIL]
        )

    def test_check_setup(self):
        self.error_handler.check_setup()
        self.assertEqual(True, True)

    def test_check_setup_no_email(self):
        self.error_handler_no_email.check_setup()
        self.assertEqual(True, True)

    def test_check_setup_no_database(self):
        try:
            self.error_handler_no_database.check_setup()
        except AttributeError as e:
            self.assertEqual(str(e), "Connection to Database not setup")
        else:
            self.fail("AttributeError not raised")

    def test_send_email(self):
        success = self.error_handler.send_error_email(
            to_email=RECEIVER_EMAIL,
            subject="Test email mzerror",
            html_content=self.sample_template.render()
        )
        self.assertTrue(success)

    def test_send_email_no_email(self):
        success = self.error_handler_no_email.send_error_email(
            to_email=RECEIVER_EMAIL,
            subject="Test email mzerror",
            html_content=self.sample_template.render()
        )
        self.assertFalse(success)

    def test_send_email_no_database(self):
        try:
            self.error_handler_no_database.send_error_email(
                to_email=RECEIVER_EMAIL,
                subject="Test email mzerror",
                html_content=self.sample_template.render()
            )
        except AttributeError as e:
            self.assertEqual(str(e), "Connection to Database not setup")
        else:
            self.fail("AttributeError not raised")

    def test_handle_error_division_by_zero(self):
        try:
            1/0
        except Exception as e:
            self.error_handler.handle_error(
                error_type_col="error_original_type",
                error_type="ZeroDivisionError",
                error_message_col="error_original_message",
                error_message=str(e),
                error_traceback_col="error_original_traceback",
                error_traceback=str(e.__traceback__),
                error_occurrence_timestamp=datetime.now(timezone.utc) - timedelta(minutes=0),
                other_dict_fields={"partner_id": 0},
                err_id_col="error_id",
                subject_email=f"Test email mzerror handle_error {datetime.now(timezone.utc)}",
                html_content=self.sample_template.render(),
            )
            self.assertEqual(True, True)

    def test_handle_error_attributes_errors(self):
        try:
            raise AttributeError("AttributeError")
        except Exception as e:
            self.error_handler.handle_error(
                error_type_col="error_original_type",
                error_type="AttributeError",
                error_message_col="error_original_message",
                error_message=str(e),
                error_traceback_col="error_original_traceback",
                error_traceback=str(e.__traceback__),
                error_occurrence_timestamp=datetime.now(timezone.utc) - timedelta(minutes=0),
                other_dict_fields={"partner_id": 0},
                err_id_col="error_id",
                subject_email=f"Test email mzerror handle_error {datetime.now(timezone.utc)}",
                html_content=self.sample_template.render(),
            )
            self.assertEqual(True, True)

    def test_handle_error_custom_error(self):
        try:
            raise Exception("CustomError")
        except Exception as e:
            self.error_handler.handle_error(
                error_type_col="error_original_type",
                error_type="CustomError",
                error_message_col="error_original_message",
                error_message=str(e),
                error_traceback_col="error_original_traceback",
                error_traceback=str(e.__traceback__),
                error_occurrence_timestamp=datetime.now(timezone.utc) - timedelta(minutes=0),
                other_dict_fields={"partner_id": 0},
                err_id_col="error_id",
                subject_email=f"Test email mzerror handle_error {datetime.now(timezone.utc)}",
                html_content=self.sample_template.render(),
            )
            self.assertEqual(True, True)

    def test_handle_error_no_email(self):
        try:
            raise AttributeError("AttributeError")
        except Exception as e:
            self.error_handler_no_email.handle_error(
                error_type_col="error_original_type",
                error_type="AttributeError",
                error_message_col="error_original_message",
                error_message=str(e),
                error_traceback_col="error_original_traceback",
                error_traceback=str(e.__traceback__),
                error_occurrence_timestamp=datetime.now(timezone.utc) - timedelta(minutes=0),
                other_dict_fields={"partner_id": 0},
                err_id_col="error_id",
                subject_email=f"Test email mzerror handle_error {datetime.now(timezone.utc)}",
                html_content=self.sample_template.render(),
            )
            self.assertEqual(True, True)
