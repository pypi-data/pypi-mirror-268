
# mzemail

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Configuration](#configuration)
    - [SMTP Setup](#smtp-setup)
    - [SendGrid Setup](#sendgrid-setup)
  - [Sending an Email](#sending-an-email)
  - [Adding Attachments](#adding-attachments)
- [Requirements](#requirements)
- [License](#license)
- [Author](#author)
- [Version](#version)

## Introduction
**mzemail** is a simple email package for Python, designed to facilitate email sending through both SMTP and SendGrid services. This flexibility makes it ideal for various applications, from simple notification systems to complex mailing solutions.

## Features
- **Flexible Email Sending**: Supports both SMTP and SendGrid.
- **Attachments Support**: Send files as attachments easily.
- **Error Handling**: Proper error responses for missing credentials or failed sends.

## Installation
To install the package, run the following pip command:

```bash
pip install mzemail
```

## Usage

### Configuration
First, configure the `MZEmail` class with your email provider's details. Here are examples for both supported modules:

#### SMTP Setup
```python
from mzemail import MZEmail

email = MZEmail(
    from_email='your-email@example.com',
    module=1, # SMTP
    smtp_server='smtp.example.com',
    smtp_port=587,
    smtp_password='yourpassword'
)
```

#### SendGrid Setup
```python
from mzemail import MZEmail

email = MZEmail(
    from_email='your-email@example.com',
    module=2, # SendGrid
    sendgrid_api_key='your-sendgrid-api-key'
)
```

### Sending an Email
You can send an email with or without attachments. Here is how you can send a basic email:

```python
email.send_email(
    to_email='recipient@example.com',
    subject='Hello, World!',
    html_content='<h1>This is a test email</h1>'
)
```

### Adding Attachments
To send an email with attachments, specify the file paths:

```python
email.send_email(
    to_email='recipient@example.com',
    subject='Report',
    html_content='<h1>See Attached Report</h1>',
    attachment_paths=['/path/to/report.pdf']
)
```

## Requirements
- Python 3.6+
- secure-smtplib
- sendgrid

## License
This project is licensed under the MIT License.

## Author
Zardin Nicolo

## Version
0.1.1
