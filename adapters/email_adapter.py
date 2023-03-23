# adapters/email_adapter.py
from entities.email import Email


class EmailAdapter:
    @staticmethod
    def from_dict(email_dict: dict) -> Email:
        return Email(
            from_address=email_dict['from_address'],
            to_address=email_dict['to_address'],
            subject=email_dict['subject'],
            body=email_dict['body']
        )