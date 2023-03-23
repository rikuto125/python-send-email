# entities/email.py
class Email:
    def __init__(self, from_address: str, to_address: str, subject: str, body: str):
        self.from_address = from_address
        self.to_address = to_address
        self.subject = subject
        self.body = body
