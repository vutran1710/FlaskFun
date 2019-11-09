from app import mail
from flask_mail import Message


def send_email(subject, recipients, text_body):
    msg = Message(subject, recipients=recipients)
    msg.body = text_body
    mail.send(msg)