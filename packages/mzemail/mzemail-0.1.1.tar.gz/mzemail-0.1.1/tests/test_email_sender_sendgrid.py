import unittest
from dotenv import find_dotenv, load_dotenv
import os
from mzemail import MZEmail

env_file = find_dotenv()
load_dotenv()

ENV = os.environ["ENV"]
PROJECT_PATH = os.environ["PROJECT_PATH"]

RECEIVER_EMAIL = os.environ["RECEIVER_EMAIL"]
SENDER_EMAIL = os.environ["SENDER_EMAIL"]
SENDGRID_API_KEY = os.environ["SENDGRID_API_KEY"]


class TestMZEmailSendgrid(unittest.TestCase):

    def setUp(self):
        self.sample_log_attachment = os.path.join(PROJECT_PATH, "tests", "test_attachments", "sample_log_attachment.log")
        self.sample_csv_attachment = os.path.join(PROJECT_PATH, "tests", "test_attachments", "sample_csv_attachment.csv")
        self.sample_pdf_attachment = os.path.join(PROJECT_PATH, "tests", "test_attachments", "sample_pdf_attachment.pdf")
        self.sample_txt_attachment = os.path.join(PROJECT_PATH, "tests", "test_attachments", "sample_txt_attachment.txt")

    def test_module_invalid(self):
        try:
            MZEmail(module="invalid_module", from_email=SENDER_EMAIL, sendgrid_api_key=SENDGRID_API_KEY)
        except ValueError as e:
            self.assertEqual(str(e), "Module used to send email is invalid")
        else:
            self.fail("ValueError not raised")

    def test_module_sendgrid(self):
        MZEmail(from_email=SENDER_EMAIL, sendgrid_api_key=SENDGRID_API_KEY)

    def test_module_sendgrid_str(self):
        MZEmail(module="sendgrid", from_email=SENDER_EMAIL, sendgrid_api_key=SENDGRID_API_KEY)

    def test_credentials_sendgrid_error(self):
        try:
            MZEmail(from_email=SENDER_EMAIL)
        except ValueError as e:
            self.assertEqual(str(e), "Missing Sendgrid credentials")
        else:
            self.fail("ValueError not raised")

    def test_send_email_sendgrid_one_email(self):
        email = MZEmail(from_email=SENDER_EMAIL, sendgrid_api_key=SENDGRID_API_KEY)
        success = email.send_email(
            to_email=RECEIVER_EMAIL,
            subject="Test email",
            html_content="This is a test email"
        )
        self.assertTrue(success)

    def test_send_email_sendgrid_multiple_email(self):
        email = MZEmail(from_email=SENDER_EMAIL, sendgrid_api_key=SENDGRID_API_KEY)
        success = email.send_email(
            to_email=RECEIVER_EMAIL.split(","),
            subject="test_send_email_sendgrid_multiple_email",
            html_content="test_send_email_sendgrid_multiple_email"
        )
        self.assertTrue(success)

    def test_send_email_sendgrid_attachment_error(self):
        email = MZEmail(from_email=SENDER_EMAIL, sendgrid_api_key=SENDGRID_API_KEY)

        with self.assertRaises(FileNotFoundError) as e:
            email.send_email(
                to_email=RECEIVER_EMAIL,
                subject="test_send_email_sendgrid_attachment_error",
                html_content="test_send_email_sendgrid_attachment_error",
                attachment_paths=["invalid_path"]
            )
            self.assertTrue(str(e), "File not found: invalid_path")

    def test_send_email_sendgrid_attachment_multiple_invalid_path(self):
        email = MZEmail(from_email=SENDER_EMAIL, sendgrid_api_key=SENDGRID_API_KEY)

        with self.assertRaises(FileNotFoundError) as e:
            email.send_email(
                to_email=RECEIVER_EMAIL,
                subject="test_send_email_sendgrid_attachment_multiple_invalid_path",
                html_content="test_send_email_sendgrid_attachment_multiple_invalid_path",
                attachment_paths=[self.sample_pdf_attachment, self.sample_csv_attachment, "invalid_path"]
            )
            self.assertTrue(str(e), "File not found: invalid_path")

    def test_send_email_sendgrid_attachment_pdf_one_email(self):
        email = MZEmail(from_email=SENDER_EMAIL, sendgrid_api_key=SENDGRID_API_KEY)
        success = email.send_email(
            to_email=RECEIVER_EMAIL.split(","),
            subject="test_send_email_sendgrid_attachment_pdf_one_email",
            html_content="test_send_email_sendgrid_attachment_pdf_one_email",
            attachment_paths=[self.sample_pdf_attachment]
        )
        self.assertTrue(success)

    def test_send_email_sendgrid_attachment_pdf_multiple_email(self):
        email = MZEmail(from_email=SENDER_EMAIL, sendgrid_api_key=SENDGRID_API_KEY)
        success = email.send_email(
            to_email=RECEIVER_EMAIL.split(","),
            subject="test_send_email_sendgrid_attachment_pdf_multiple_email",
            html_content="test_send_email_sendgrid_attachment_pdf_multiple_email",
            attachment_paths=[self.sample_pdf_attachment]
        )
        self.assertTrue(success)

    def test_send_email_sendgrid_attachment_csv_one_email(self):
        email = MZEmail(from_email=SENDER_EMAIL, sendgrid_api_key=SENDGRID_API_KEY)
        success = email.send_email(
            to_email=RECEIVER_EMAIL.split(","),
            subject="test_send_email_sendgrid_attachment_csv_one_email",
            html_content="test_send_email_sendgrid_attachment_csv_one_email",
            attachment_paths=[self.sample_csv_attachment]
        )
        self.assertTrue(success)

    def test_send_email_sendgrid_attachment_csv_multiple_email(self):
        email = MZEmail(from_email=SENDER_EMAIL, sendgrid_api_key=SENDGRID_API_KEY)
        success = email.send_email(
            to_email=RECEIVER_EMAIL.split(","),
            subject="test_send_email_sendgrid_attachment_csv_multiple_email",
            html_content="test_send_email_sendgrid_attachment_csv_multiple_email",
            attachment_paths=[self.sample_csv_attachment]
        )
        self.assertTrue(success)

    def test_send_email_sendgrid_attachment_txt_one_email(self):
        email = MZEmail(from_email=SENDER_EMAIL, sendgrid_api_key=SENDGRID_API_KEY)
        success = email.send_email(
            to_email=RECEIVER_EMAIL.split(","),
            subject="test_send_email_sendgrid_attachment_txt_one_email",
            html_content="test_send_email_sendgrid_attachment_txt_one_email",
            attachment_paths=[self.sample_txt_attachment]
        )
        self.assertTrue(success)

    def test_send_email_sendgrid_attachment_txt_multiple_email(self):
        email = MZEmail(from_email=SENDER_EMAIL, sendgrid_api_key=SENDGRID_API_KEY)
        success = email.send_email(
            to_email=RECEIVER_EMAIL.split(","),
            subject="test_send_email_sendgrid_attachment_txt_multiple_email",
            html_content="test_send_email_sendgrid_attachment_txt_multiple_email",
            attachment_paths=[self.sample_txt_attachment]
        )
        self.assertTrue(success)

    def test_send_email_sendgrid_attachment_log_one_email(self):
        email = MZEmail(from_email=SENDER_EMAIL, sendgrid_api_key=SENDGRID_API_KEY)
        success = email.send_email(
            to_email=RECEIVER_EMAIL,
            subject="test_send_email_sendgrid_attachment_log_one_email",
            html_content="test_send_email_sendgrid_attachment_log_one_email",
            attachment_paths=[self.sample_log_attachment]
        )
        self.assertTrue(success)

    def test_send_email_sendgrid_attachment_log_multiple_email(self):
        email = MZEmail(from_email=SENDER_EMAIL, sendgrid_api_key=SENDGRID_API_KEY)
        success = email.send_email(
            to_email=RECEIVER_EMAIL,
            subject="test_send_email_sendgrid_attachment_log_multiple_email",
            html_content="test_send_email_sendgrid_attachment_log_multiple_email",
            attachment_paths=[self.sample_log_attachment]
        )
        self.assertTrue(success)

    def test_send_email_sendgrid_attachment_multiple_one_email(self):
        email = MZEmail(from_email=SENDER_EMAIL, sendgrid_api_key=SENDGRID_API_KEY)
        success = email.send_email(
            to_email=RECEIVER_EMAIL,
            subject="test_send_email_sendgrid_attachment_multiple_one_email",
            html_content="test_send_email_sendgrid_attachment_multiple_one_email",
            attachment_paths=[self.sample_pdf_attachment, self.sample_csv_attachment, self.sample_txt_attachment, self.sample_log_attachment]
        )
        self.assertTrue(success)

    def test_send_email_sendgrid_attachment_multiple_multiple_email(self):
        email = MZEmail(from_email=SENDER_EMAIL, sendgrid_api_key=SENDGRID_API_KEY)
        success = email.send_email(
            to_email=RECEIVER_EMAIL.split(","),
            subject="test_send_email_sendgrid_attachment_multiple_multiple_email",
            html_content="test_send_email_sendgrid_attachment_multiple_multiple_email",
            attachment_paths=[self.sample_pdf_attachment, self.sample_csv_attachment, self.sample_txt_attachment, self.sample_log_attachment]
        )
        self.assertTrue(success)