# adapters/smtp_adapter.py
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
from usecases.email_dto import EmailDTO


class SmtpAdapter:
    def __init__(self, smtp_host: str, smtp_port: int, smtp_username: str, smtp_password: str):
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
        self.smtp_username = smtp_username
        self.smtp_password = smtp_password

    def send_email(self, email: EmailDTO):
        print(email)
        msg = MIMEText(email.body)
        # メールの作成
        msg['Subject'] = email.subject
        msg['From'] = email.from_address
        msg['To'] = email.to_address
        msg['Date'] = formatdate()

        # メールの送信
        smtp_obj = smtplib.SMTP(self.smtp_host, self.smtp_port)
        smtp_obj.starttls()
        smtp_obj.login(self.smtp_username, self.smtp_password)
        smtp_obj.sendmail(email.from_address, email.to_address, msg.as_string())
        smtp_obj.quit()
