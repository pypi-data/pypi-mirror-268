import unittest

from tests.test_email_sender_sendgrid import TestMZEmailSendgrid
from tests.test_email_sender_smtplib import TestMZEmailSMTPLib


class TestHandler(unittest.TestCase):

    test_cases = [
        TestMZEmailSendgrid,
        TestMZEmailSMTPLib
    ]

    def test_handler(self):
        for test_case in self.test_cases:
            suite = unittest.TestLoader().loadTestsFromTestCase(test_case)
            unittest.TextTestRunner(verbosity=2).run(suite)
