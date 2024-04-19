# mzerror

[![PyPI version](https://badge.fury.io/py/mzerror.svg)](https://badge.fury.io/py/mzerror/) 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Features](#features)
- [Usage](#usage)
  - [Error Handling Setup](#error-handling-setup)
  - [Email Configuration](#email-configuration)
  - [Database Configuration](#database-configuration)
  - [Handling Errors](#handling-errors)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)
- [Contact](#contact)
- [Version](#version)

## Description
This Python package provides an `ErrorHandler` class designed to handle errors, log them in a database, and send emails for critical issues. The package is equipped with functionalities to manage email settings, database connections, and error handling.

## Installation
You can install the package using pip:

```bash
pip install mzerror
```

## Features
- **Error Logging**: Automatically logs errors to a specified database.
- **Email Notifications**: Sends email notifications for critical errors using the `MZEmail` package.
- **Flexible Configuration**: Supports configuration through parameters or environment variables.

## Usage

### Error Handling Setup
Initialize the `ErrorHandler` class with the necessary parameters:

```python
from mzerror import ErrorHandler
error_handler = ErrorHandler(script_name='example_script.py', script_path='/path/to/script')
```

### Email Configuration
Configure the email settings using `setup_email` method:

```python
error_handler.setup_email(
    from_email='your-email@example.com',
    module=2, # Using SendGrid
    sendgrid_api_key='your-sendgrid-api-key',
    emails_receivers=['admin@example.com']
)
```

### Database Configuration
Set up the database connection to log errors:

```python
error_handler.setup_connection(
    host='localhost',
    username='user',
    password='password',
    database='errors_db',
    error_log_table_name='error_logs',
    error_table_name='errors'
)
```

### Handling Errors
Handle an error and possibly send an email if the error is critical:

```python
try:
    # Your code that might throw an exception
    raise ValueError("An example error.")
except Exception as e:
    error_handler.handle_error(
        error_type_col='type',
        error_type=str(type(e)),
        error_message_col='message',
        error_message=str(e),
        error_traceback_col='traceback',
        error_traceback=str(e.__traceback__)
    )
```

## Dependencies
- mzemail
- mysql-connector-python
- jinja2

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
Zardin Nicolo

## Contact
For any queries, you can reach out to [Zardin Nicolo](mailto:zardin.nicolo@gmail.com).

## Version
0.1.1

