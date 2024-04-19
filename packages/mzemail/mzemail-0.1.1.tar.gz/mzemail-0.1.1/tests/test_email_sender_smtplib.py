import unittest
from dotenv import find_dotenv, load_dotenv
import os
from mzemail import MZEmail

env_file = find_dotenv()
load_dotenv()

ENV = os.environ["ENV"]
PROJECT_PATH = os.environ["PROJECT_PATH"]

RECEIVER_EMAIL = os.environ["RECEIVER_EMAIL"]

SENDER_EMAIL_SMTPLIB = os.environ["SENDER_EMAIL_SMTPLIB"]
SENDER_EMAIL_PASSWORD = os.environ["SENDER_EMAIL_PASSWORD"]
SMTP_SERVER = os.environ["SMTP_SERVER"]
SMTP_PORT = int(os.environ["SMTP_PORT"])


class TestMZEmailSMTPLib(unittest.TestCase):

    def setUp(self):
        self.sample_log_attachment = os.path.join(PROJECT_PATH, "tests", "test_attachments", "sample_log_attachment.log")
        self.sample_csv_attachment = os.path.join(PROJECT_PATH, "tests", "test_attachments", "sample_csv_attachment.csv")
        self.sample_pdf_attachment = os.path.join(PROJECT_PATH, "tests", "test_attachments", "sample_pdf_attachment.pdf")
        self.sample_txt_attachment = os.path.join(PROJECT_PATH, "tests", "test_attachments", "sample_txt_attachment.txt")

    def test_module_invalid(self):
        try:
            MZEmail(module="invalid_module", from_email=SENDER_EMAIL_SMTPLIB, smtp_server=SMTP_SERVER, smtp_port=SMTP_PORT, smtp_password=SENDER_EMAIL_PASSWORD)
        except ValueError as e:
            self.assertEqual(str(e), "Module used to send email is invalid")
        else:
            self.fail("ValueError not raised")

    def test_module_smtplib(self):
        MZEmail(module=1, from_email=SENDER_EMAIL_SMTPLIB, smtp_server=SMTP_SERVER, smtp_port=SMTP_PORT, smtp_password=SENDER_EMAIL_PASSWORD)

    def test_module_smtplib_str(self):
        MZEmail(module="smtplib", from_email=SENDER_EMAIL_SMTPLIB, smtp_server=SMTP_SERVER, smtp_port=SMTP_PORT, smtp_password=SENDER_EMAIL_PASSWORD)

    def test_credentials_smtplib_error(self):
        try:
            MZEmail(module=1, from_email=SENDER_EMAIL_SMTPLIB)
        except ValueError as e:
            self.assertEqual(str(e), "Missing SMTP credentials")
        else:
            self.fail("ValueError not raised")

    def test_send_email_smtplib_one_email(self):
        email = MZEmail(module=1, from_email=SENDER_EMAIL_SMTPLIB, smtp_server=SMTP_SERVER, smtp_port=SMTP_PORT, smtp_password=SENDER_EMAIL_PASSWORD)
        success = email.send_email(
            to_email=RECEIVER_EMAIL,
            subject="test_send_email_smtplib_one_email",
            html_content="test_send_email_smtplib_one_email"
        )
        self.assertTrue(success)

    def test_send_email_smtplib_multiple_emails(self):
        email = MZEmail(module=1, from_email=SENDER_EMAIL_SMTPLIB, smtp_server=SMTP_SERVER, smtp_port=SMTP_PORT, smtp_password=SENDER_EMAIL_PASSWORD)
        success = email.send_email(
            to_email=RECEIVER_EMAIL,
            subject="test_send_email_smtplib_multiple_emails",
            html_content="test_send_email_smtplib_multiple_emails"
        )
        self.assertTrue(success)

    def test_send_email_smtplib_one_email_with_attachment(self):
        email = MZEmail(module=1, from_email=SENDER_EMAIL_SMTPLIB, smtp_server=SMTP_SERVER, smtp_port=SMTP_PORT, smtp_password=SENDER_EMAIL_PASSWORD)
        success = email.send_email(
            to_email=RECEIVER_EMAIL,
            subject="test_send_email_smtplib_one_email_with_attachment",
            html_content="test_send_email_smtplib_one_email_with_attachment",
            attachment_paths=[self.sample_log_attachment]
        )
        self.assertTrue(success)

    def test_send_email_smtplib_multiple_emails_with_attachment(self):
        email = MZEmail(module=1, from_email=SENDER_EMAIL_SMTPLIB, smtp_server=SMTP_SERVER, smtp_port=SMTP_PORT, smtp_password=SENDER_EMAIL_PASSWORD)
        success = email.send_email(
            to_email=RECEIVER_EMAIL,
            subject="test_send_email_smtplib_multiple_emails_with_attachment",
            html_content="test_send_email_smtplib_multiple_emails_with_attachment",
            attachment_paths=[self.sample_log_attachment]
        )
        self.assertTrue(success)

    def test_send_email_smtplib_one_email_with_multiple_attachments(self):
        email = MZEmail(module=1, from_email=SENDER_EMAIL_SMTPLIB, smtp_server=SMTP_SERVER, smtp_port=SMTP_PORT, smtp_password=SENDER_EMAIL_PASSWORD)
        success = email.send_email(
            to_email=RECEIVER_EMAIL,
            subject="test_send_email_smtplib_one_email_with_multiple_attachments",
            html_content="test_send_email_smtplib_one_email_with_multiple_attachments",
            attachment_paths=[self.sample_log_attachment, self.sample_csv_attachment, self.sample_pdf_attachment, self.sample_txt_attachment]
        )
        self.assertTrue(success)