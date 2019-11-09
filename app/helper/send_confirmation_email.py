import os
from flask import url_for
from itsdangerous import URLSafeTimedSerializer
from app.helper.send_email import send_email
from app.api import register


confirm_serializer = URLSafeTimedSerializer(os.getenv('SECRET_KEY'))


def generate_confirmation_token(user_email):
    return confirm_serializer.dumps(user_email, salt=os.getenv('SECURITY_PASSWORD_SALT'))


def send_confirmation_email(user_email, confirmation_token):
    confirm_url = url_for('register.confirm_email', token=confirmation_token, _external=True)

    send_email('Confirm Your Email Address', [user_email], confirm_url)
