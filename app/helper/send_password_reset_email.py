import os
import datetime
from flask import url_for
import jwt
from app.helper.send_email import send_email
from app.api import register # noqa
from app import jinja_env


def generate_reset_token(user_id, user_email):
    payload = {
        'id': user_id,
        'email': user_email,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=30)
    }
    return jwt.encode(payload, os.getenv('JWT_SECRET_KEY'), algorithm='HS256')


def send_password_reset_email(user_email, confirmation_token):
    password_reset_url = url_for('register.confirm_email', token=confirmation_token, _external=True)
    template = jinja_env.get_template('email_password_reset.html')
    html = template.render(password_reset_url=password_reset_url)
    send_email('Password Reset Requested', [user_email], html)
