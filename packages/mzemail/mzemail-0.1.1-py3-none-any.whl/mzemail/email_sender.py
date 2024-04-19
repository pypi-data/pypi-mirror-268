import base64
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from sendgrid.helpers.mail import Attachment


class MZEmail:

    email_module = {
        '1': 'smtplib',
        '2': 'sendgrid'
    }

    def __init__(self, from_email: str, **kwargs):
        """
        Create an instance of EmailManager.

        Parameters:
            from_email: (str) from username used to send the email.

            --- Passing through **kwargs ---
            module: (int) name of the module used to send the email, the module accepted are: smtplib(1) and sendgrid(2). Default is sendgrid.
            smtp_server: (str, optional) smtp server used to send the email, must set if module is smtplib.
            smtp_port: (int, optional) smtp port used to send the email, must set if module is smtplib.
            smtp_password: (str, optional) smtp password used to send the email, must set if module is smtplib.
            sendgrid_api_key: (str, optional) sendgrid api key used to send the email, must set if module is sendgrid.

        Raises:
            ValueError: If module to send email is invalid.
                        If email credentials are not set.
        """
        self.module = kwargs.get('module', 2)
        self._check_module()

        self.smtp_server = kwargs.get('smtp_server')
        self.smtp_port = kwargs.get('smtp_port')
        self.from_email = from_email
        self.smtp_password = kwargs.get('smtp_password')
        self.sendgrid_api_key = kwargs.get('sendgrid_api_key')
        self._check_credentials()

    def _check_module(self):
        """
        Check if module are valid.

        Raises:
            ValueError: If module to send email is invalid.
        """
        if str(self.module) not in self.email_module:
            raise ValueError("Module used to send email is invalid")
        else:
            self.module = self.email_module[str(self.module)]

    def _check_credentials(self):
        """
        Check if email credentials are set.

        Raises:
            ValueError: If email credentials are not set.
        """
        if self.module == 'smtplib':
            if not self.smtp_server or not self.smtp_port or not self.from_email or not self.smtp_password:
                raise ValueError("Missing SMTP credentials")
        elif self.module == 'sendgrid':
            if not self.sendgrid_api_key or not self.from_email:
                raise ValueError("Missing Sendgrid credentials")

    def send_email(self, to_email: list or str, subject: str, html_content: str, attachment_paths: list = None):
        """
        Send email.

        Parameters:
            to_email: (list[str] or str) email address of the recipient, if multiple email addresses are provided, they must be in a list for sendgrid otherwise the mail
                                        will be sent to the first email address only.
            subject: (str) subject of the email.
            html_content: (str) html content of the email.
            attachment_paths: (list[str], optional) list of file paths to be attached to the email.

        Returns: (bool) True if email is sent successfully, False otherwise.\

        Raises:
            FileNotFoundError: If file to be attached is not found.
            Exception: If error occurred while sending email.
        """
        success = False

        if self.module == 'smtplib':
            success = self.send_email_smtp(to_email, subject, html_content, attachment_paths)
        elif self.module == 'sendgrid':
            success = self.send_email_sendgrid(to_email, subject, html_content, attachment_paths)

        return success

    def send_email_smtp(self, to_email: list or str, subject: str, html_content: str, attachment_paths: list = None) -> bool:
        """
        Send email using smtplib.

        Parameters:
            to_email: (list[str] or str) email address of the recipient.
            subject: (str) subject of the email.
            html_content: (str) html content of the email.
            attachment_paths: (list[str], optional) list of file paths to be attached to the email.

        Returns:
            (bool) True if email is sent successfully, False otherwise.

        Raises:
            FileNotFoundError: If file to be attached is not found.
            Exception: If error occurred while sending email.
        """
        msg = MIMEMultipart()
        msg['From'] = self.from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(html_content, 'html'))

        if attachment_paths:
            for file_path in attachment_paths:
                try:
                    with open(file_path, 'rb') as f:
                        attachment = MIMEApplication(f.read())
                        attachment.add_header('Content-Disposition', 'attachment', filename=file_path)
                        msg.attach(attachment)
                except FileNotFoundError:
                    raise FileNotFoundError("File not found:", file_path)

        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.from_email, self.smtp_password)
            server.sendmail(self.from_email, to_email, msg.as_string())
            server.quit()
        except Exception as e:
            raise Exception("Error sending email:", str(e))

        return True

    def send_email_sendgrid(self, to_email: list or str, subject: str, html_content: str, attachment_paths: list = None) -> bool:
        """
        Send email via SendGrid.

        Parameters:
            to_email: (list[str] or str) list of email addresses to send the email.
            subject: (str) subject of the email.
            html_content: (str) html content of the email.
            attachment_paths: (list[str]) list of file paths to be attached.

        Returns:
            (bool) True if email is sent successfully, False otherwise.

        Raises:
            FileNotFoundError: If file to be attached is not found.
            Exception: If error occurred while sending email.
        """

        message = Mail(
            from_email=self.from_email,
            to_emails=to_email,
            subject=subject,
            html_content=html_content)

        if attachment_paths:
            lst_attachments = []
            for file_path in attachment_paths:
                try:
                    with open(file_path, 'rb') as f:
                        attachment = Attachment()
                        attachment.file_content = base64.b64encode(f.read()).decode()
                        # attachment.file_type = 'application/octet-stream'
                        attachment.file_name = os.path.basename(file_path)
                        attachment.disposition = 'attachment'
                        lst_attachments.append(attachment)
                        # message.attachment.append(attachment)
                except FileNotFoundError:
                    raise FileNotFoundError("File not found:", file_path)

            message.attachment = lst_attachments
        try:
            sg = SendGridAPIClient(self.sendgrid_api_key)
            response = sg.send(message)
            if response.status_code != 202:
                print("Failed to send email via SendGrid:", response.body)
                return False
        except Exception as e:
            raise Exception("Error sending email:", str(e))

        return True
