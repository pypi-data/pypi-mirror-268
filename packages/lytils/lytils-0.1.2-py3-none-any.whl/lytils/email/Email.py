# Third-party Libraries
import smtplib
from email.message import EmailMessage
from lytils.surfshark import Surfshark


class Email:
    def __init__(self, smtp, credentials, surfshark_path: str = "", notify: str = ""):
        """
        :param smtp dict:
            Expects 'server' key (ex. 'smtp.example.com')
            Expects 'port' key (default: 587)
        :param credentials dict:
            Expects 'email' key; email used to send the email
            Expects 'password' key; password for sender's email
        :param notify string:
            Instead of having to pass a recipient email to
            send_email every time, you can declare a default
            email, and use notify() to send email to that recipient
        """
        self._smtp = smtp

        # Set port by default if not specified
        if "port" not in smtp:
            self._smtp["port"] = 587

        self._surfshark = None
        if surfshark_path:
            self._surfshark = Surfshark(surfshark_path)

        self._creds = credentials
        self._notify = notify
        self._server = None

    def start_server(self):
        # Kill surfshark if it is running as it blocks SMTP connections.
        if self._surfshark and self._surfshark.running():
            self._surfshark.kill()

        # Connect to the SMTP server
        self._server = smtplib.SMTP("smtp.gmail.com", 587)
        # self._server = smtplib.SMTP(smtp['server'], smtp['port'])
        # self._server.ehlo()
        self._server.starttls()
        self._server.login(self._creds["email"], self._creds["password"])

    def send_email(self, recipient, subject, message):
        # Create the email
        msg = EmailMessage()
        msg.set_content(message)
        msg["subject"] = subject
        msg["to"] = recipient
        msg["from"] = self._creds["email"]

        # Send the email
        self._server.sendmail(self._creds["email"], recipient, msg.as_string())

    def notify(self, subject, message):
        if self._notify:
            self.send_email(self._notify, subject, message)

    def quit(self):
        if self._server:
            self._server.quit()

        # Restart surfshark if it is not currently running.
        if self._surfshark and not self._surfshark.running():
            self._surfshark.start()
