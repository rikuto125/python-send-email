# usecases/send_email.py
from adapters.smtp_adapter import SmtpAdapter
from entities.email import Email
from usecases.email_dto import EmailDTO


class SendEmailUseCase:
    def __init__(self, smtp_adapter: SmtpAdapter):
        self.smtp_adapter = smtp_adapter

    def execute(self, from_address: str, to_address: str, subject: str, body: str):
        email = Email(from_address, to_address, subject, body)
        email_dto = EmailDTO(email.from_address, email.to_address, email.subject, email.body)
        self.smtp_adapter.send_email(email_dto)
