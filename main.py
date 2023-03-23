# main.py
from adapters.smtp_adapter import SmtpAdapter
from usecases.send_email import SendEmailUseCase

if __name__ == '__main__':

    smtp_host = 'smtp.example.com'
    smtp_port = 587
    smtp_username = 'your_username'
    smtp_password = 'your_password'

    smtp_adapter = SmtpAdapter(smtp_host, smtp_port, smtp_username, smtp_password)
    send_email_usecase = SendEmailUseCase(smtp_adapter)

    from_address = 'from@example.com'
    to_address = 'to@example.com'
    subject = 'Test Email'
    body = 'This is a test email'

    send_email_usecase.execute(from_address, to_address, subject, body)
