import os
import datetime
from flask import url_for
import jwt
from app.helper.send_email import send_email
from app.api import register # noqa
from app import jinja_env


def generate_confirmation_token(user_id, user_email):
    payload = {
        'id': user_id,
        'email': user_email,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=30)
    }
    return jwt.encode(payload, os.getenv('JWT_SECRET_KEY'), algorithm='HS256')


def send_confirmation_email(user_email, confirmation_token):
    confirm_url = url_for('register.confirm_email', token=confirmation_token, _external=True)
    template = jinja_env.get_template('email-confirmation.html')
    html = template.render(confirm_url=confirm_url)
    send_email('Confirm Your Email Address', [user_email], html)
