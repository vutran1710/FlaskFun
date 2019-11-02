from flask import url_for
from itsdangerous import URLSafeTimedSerializer
from app.helper.send_email import send_email
from app.api import register


confirm_serializer = URLSafeTimedSerializer('SECRET_KEY')


def send_confirmation_email(user_email):

    confirm_url = url_for(
        'register.confirm_email',
        token=confirm_serializer.dumps(user_email, salt='email-confirmation-salt'),
        _external=True)

    send_email('Confirm Your Email Address', [user_email], confirm_url)
