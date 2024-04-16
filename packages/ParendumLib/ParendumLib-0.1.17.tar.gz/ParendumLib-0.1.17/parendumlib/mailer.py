from typing import Tuple, Dict, List, Optional, Union
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate
from jinja2 import Template
import smtplib
import imaplib
import email


class GMailer:

    def __init__(self, email_address: str, password: str, imap_server: str = 'imap.gmail.com'):
        self.email = email_address
        self.password = password
        self.imap_server = imap_server
        self._mail = None

    def send_email(self, config: dict, to: str, subject: str, template_file: str, context: dict):
        try:
            with open(template_file, "r") as file:
                template_content = file.read()

            template = Template(template_content)
            template = template.render(context)

            msg = MIMEMultipart()
            msg['From'] = config.get('email', dict()).get('username')
            msg['To'] = to
            msg['Subject'] = subject
            msg['Date'] = formatdate(localtime=True)

            msg.attach(MIMEText(template, 'html'))

            try:
                server = smtplib.SMTP(config.get('email', dict()).get('server'),
                                      config.get('email', dict()).get('port'))
            except Exception as e:
                print(f"Error al conectar al servidor SMTP: {e}")
                return False
            try:
                server.starttls()
            except Exception as e:
                print(f"Error al iniciar TLS: {e}")
                return False
            server.login(config.get('email', dict()).get('username'), config.get('email', dict()).get('password'))
            server.sendmail(config.get('email', dict()).get('username'), to, msg.as_string())
            server.quit()
            return True
        except Exception as e:
            print(f"[EXCEPTION] {str(e)} - Sending Email Template")
        return False

    def find_emails(self, target_email: str, search_flag: str = 'FROM', target_folder: str = 'inbox') -> list:
        if search_flag not in ['TO', 'FROM']:
            raise ValueError("search_flag must be 'TO' or 'FROM'")
        self._connect(target_folder)
        _search = f'({search_flag} "{target_email}")'
        result, data = self._mail.search(None, _search)
        if result != "OK":
            return []
        if not (email_ids := data[0].split()):
            return []
        return email_ids

    def read_email(self, email_id: str) -> Dict[str, Optional[Union[str, List[Tuple[str, str]]]]]:
        _, email_data = self._mail.fetch(email_id, '(RFC822)')
        raw_email = email_data[0][1]
        email_message = email.message_from_bytes(raw_email)

        result = {
            "text": None,
            "html": None,
            "headers": self._get_headers(email_message),
            "attachments": self._get_attachments(email_message)
        }

        for part in email_message.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition"))

            if "attachment" in content_disposition:
                continue
            elif content_type == "text/plain" and not result["text"]:
                result["text"] = part.get_payload(decode=True).decode()
            elif content_type == "text/html" and not result["html"]:
                result["html"] = part.get_payload(decode=True).decode()

        return result

    def delete_emails(self, target_email: str, search_flag: str = 'FROM', target_folder: str = 'inbox'):
        self._connect(target_folder)
        for e_id in self.find_emails(target_email, search_flag, target_folder):
            self._delete_email(e_id)
        self._mail.expunge()
        self._mail.close()
        self._mail.logout()

    def _connect(self, target_folder: str = 'inbox'):
        self._mail = imaplib.IMAP4_SSL(self.imap_server)
        self._mail.login(self.email, self.password)
        self._mail.select(target_folder)

    def _delete_email(self, email_id: str):
        self._mail.store(email_id, '+FLAGS', '\\Deleted')

    @staticmethod
    def _get_headers(email_message) -> Dict[str, str]:
        return {key: value for key, value in email_message.items()}

    @staticmethod
    def _get_attachments(email_message) -> List[Tuple[str, str]]:
        attachments = []
        for part in email_message.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue

            filename = part.get_filename()
            if filename:
                payload = part.get_payload(decode=True)
                attachments.append((filename, payload))
        return attachments


if __name__ == '__main__':
    mailer = GMailer("parendumou@gmail.com", "laeujjrdrxhwqnjo")
