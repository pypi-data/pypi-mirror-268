from datetime import datetime, timezone

from mzemail import MZEmail

from .mysql_connection import MySQLConnection


class ErrorHandler:
    """
    This class is used to handle errors and send emails
    """

    def __init__(self, **kwargs):
        """
                Create an instance of EmailManager.

                Parameters:
                    --- Passing through kwargs ---
                    script_name: (str) name of the script that is using the error handler.
                    script_path: (str) path of the script that is using the error handler.
                    default_minutely_error_send: (int, optional) default minutes to send email if error is not handled.
                    is_send_email: (bool, optional) if True send email, else not send email.
                """
        self.script_name = kwargs.get('script_name')
        self.script_path = kwargs.get('script_path')
        self.default_minutely_error_send = kwargs.get('default_minutely_error_send', 60)
        self.is_send_email = kwargs.get('is_send_email', True)

        self.connection = None
        self.host = None
        self.username = None
        self.password = None
        self.database = None
        self.error_log_table_name = None
        self.error_table_name = None

        self.email = None
        self.emails_receivers = None

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()

    def setup_email(self, **kwargs):
        """
        Setup email to send using MZEmail.

        Parameters:
            --- Passing through kwargs ---
            MZEmail: (instance) instance of MZEmail.
            from_email: (str) from username used to send the email.
            module: (int) name of the module used to send the email, the module accepted are: smtplib(1) and sendgrid(2). Default is sendgrid.
            smtp_server: (str) smtp server used to send the email, must set if module is smtplib.
            smtp_port: (int) smtp port used to send the email, must set if module is smtplib.
            smtp_password: (str) smtp password used to send the email, must set if module is smtplib.
            sendgrid_api_key: (str) sendgrid api key used to send the email, must set if module is sendgrid.
            emails_receivers: (list) list of emails to send.

        Raises:
            ValueError: If module to send email is invalid.
                        If email credentials are not set.
        """
        self.email = kwargs.get('MZEmail',
                                MZEmail(from_email=kwargs.get('from_email'), module=kwargs.get('module'),
                                        smtp_server=kwargs.get('smtp_server'),
                                        smtp_port=kwargs.get('smtp_port'), smtp_password=kwargs.get('smtp_password'),
                                        sendgrid_api_key=kwargs.get('sendgrid_api_key')))

        self.emails_receivers = kwargs.get('emails_receivers')

    def setup_connection(self, **kwargs):
        """
        Setup connection to database and set errors table name.

        Parameters:
            --- Passing through kwargs ---
            host: (str) host of the database.
            username: (str) username of the database.
            password: (str) password of the database.
            database: (str) database name.
            error_log_table_name: (str) error log table name.
            error_table_name: (str) error table name.
        """
        self.host = kwargs.get('host')
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')
        self.database = kwargs.get('database')
        self.error_log_table_name = kwargs.get('error_log_table_name')
        self.error_table_name = kwargs.get('error_table_name')

        if self.host and self.username and self.password and self.database and self.error_log_table_name:
            self.connection = MySQLConnection(host=self.host, username=self.username, password=self.password,
                                              database=self.database)

    def check_setup(self):
        """
        Check if setup is done.

        Raises:
            Exception: If email is not setup.
                       If connection to database is not setup.
        """
        if not self.email and self.is_send_email:
            raise AttributeError("Email not setup")
        if not self.host or not self.username or not self.password or not self.database \
                or not self.error_log_table_name:
            raise AttributeError("Connection to Database not setup")
        if not self.connection:
            raise AttributeError("Connection to Database not setup")

    def get_error_information(self, err_id: int) -> tuple:
        """
        Get error information from database.

        Parameters:
            err_id: (int) error id.

        Returns:
            error_repeat_minutes_range_local: (int) error repeat minutes range local.
            error_is_handled_default: (bool) error is handled default.
            error_email_address_to_send: (list) list of emails to send.

        Raises:
            AttributeError: If error table name is not setup.
        """
        error_repeat_minutes_range_local, error_is_handled_default, error_email_address_to_send = self.default_minutely_error_send, False, self.emails_receivers

        if err_id != -1:
            if self.error_table_name is None:
                raise AttributeError("Error mapped table name not setup")

            mapped_err = self.connection.select(table_name=self.error_table_name,
                                                select_columns=['error_repeat_minutes_range_local',
                                                                'error_is_handled_default',
                                                                'error_email_address_to_send_local'],
                                                columns=['id'], values=[err_id])

            if mapped_err:
                mapped_err = mapped_err[0]
                error_repeat_minutes_range_local = mapped_err['error_repeat_minutes_range_local']
                error_is_handled_default = mapped_err['error_is_handled_default']
                error_email_address_to_send = mapped_err['error_email_address_to_send_local'].replace(" ", "").split(
                    ",")

        return error_repeat_minutes_range_local, error_is_handled_default, error_email_address_to_send

    def handle_error(self, error_type_col: str, error_type: str, error_message_col: str, error_message: str,
                     error_traceback_col: str, error_traceback: str = None,
                     error_occurrence_timestamp: datetime = None, other_dict_fields: dict = None,
                     err_id_col: str = None, err_id: int = 0,
                     subject_email: str = None, html_content: str = None, attachments_files: list = None) -> None:
        """
        Handle error and send email.

        Parameters:
            error_type_col: (str) error type column name.
            error_type: (str) error type.
            error_message_col: (str) error message column name.
            error_message: (str) error message.
            error_traceback_col: (str) error traceback column name.
            error_traceback: (str, optional) error traceback.
            error_occurrence_timestamp: (datetime, optional) error occurrence timestamp.
            other_dict_fields: (dict, optional) other fields to insert in database.
            err_id_col: (str, optional) error id column name.
            err_id: (int, optional) error id, default is 0 (database mapped error "UNKNOWN_ERROR"). If err_id is -1, error is not mapped, ignore the database search.
            subject_email: (str, optional) subject of the email.
            html_content: (str, optional) html content of the email, must be a jinja2 template.render().
            attachments_files: (list, optional) list of files to attach to the email.

        Raises:
            AttributeError: If error table name is not setup.
            AttributeError: If subject and html content are not setup.
        """
        self.check_setup()

        if not error_occurrence_timestamp:
            error_occurrence_timestamp = datetime.now(timezone.utc)

        if not other_dict_fields:
            other_dict_fields = {}

        error_type = error_type.replace("'", "").replace('"', '') if error_type else None
        error_message = error_message.replace("'", "").replace('"', '') if error_message else None
        error_traceback = error_traceback.replace("'", "").replace('"', '') if error_traceback else None

        other_dict_fields[error_type_col] = error_type
        other_dict_fields[error_message_col] = error_message
        other_dict_fields[error_traceback_col] = error_traceback
        other_dict_fields['script_path'] = self.script_path
        other_dict_fields['script_name'] = self.script_name

        is_send_email = self.is_send_email

        error_repeat_minutes_range_local, error_is_handled_default, error_email_address_to_send = self.get_error_information(
            err_id)

        last_err = self.connection.get_last_error(error_log_table_name=self.error_log_table_name, err_id_col=err_id_col,
                                                  err_id=err_id,
                                                  error_type_col=error_type_col, error_type=error_type,
                                                  error_message_col=error_message_col, error_message=error_message,
                                                  error_script_path=self.script_path,
                                                  error_occurrence_timestamp=error_occurrence_timestamp,
                                                  error_repeat_minutes_range_local=error_repeat_minutes_range_local)

        if not last_err:

            if is_send_email:

                if not subject_email or not html_content:
                    raise AttributeError("Subject and html content not setup")

                self.email.send_email(to_email=error_email_address_to_send,
                                      subject=subject_email,
                                      html_content=html_content,
                                      attachment_paths=attachments_files)

            other_dict_fields[err_id_col] = err_id
            other_dict_fields['error_first_occurrence_timestamp_utc'] = error_occurrence_timestamp
            other_dict_fields['error_last_occurrence_timestamp_utc'] = error_occurrence_timestamp
            other_dict_fields['error_number_of_occurrences'] = 1
            other_dict_fields['error_email_address_sent'] = ', '.join(error_email_address_to_send)

            self.connection.insert(table_name=self.error_log_table_name, columns=list(other_dict_fields.keys()),
                                   values=list(other_dict_fields.values()))

        else:
            self.connection.update(table_name=self.error_log_table_name,
                                   params={'error_last_occurrence_timestamp_utc': error_occurrence_timestamp,
                                           'error_number_of_occurrences': last_err['error_number_of_occurrences'] + 1,
                                           'error_is_handled': error_is_handled_default},
                                   conditions={'id': last_err['id']})

    def send_error_email(self, to_email, subject: str, html_content: str,
                         attachment_paths: list = None) -> bool:
        """
        Send error email.

        Parameters:
            to_email: (str) email address to send.
            subject: (str) subject of the email.
            html_content: (str) html content of the email, must be a jinja2 template.render().
            attachment_paths: (list, optional) list of files to attach to the email.

        Returns:
            success: (bool) True if email is sent, else False.
        """
        self.check_setup()
        if self.is_send_email:
            success = self.email.send_email(to_email=to_email,
                                            subject=subject,
                                            html_content=html_content,
                                            attachment_paths=attachment_paths)
            return success

        return False
