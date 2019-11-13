import os
from flask import request, Blueprint, jsonify
from sqlalchemy import exc
import jwt
from werkzeug.exceptions import BadRequest
from app.models import User, UserProfile
from app import db, bcrypt
from app.decorator import schema_required
from app.helper.send_confirmation_email import generate_confirmation_token, send_confirmation_email
from app.user_schema import schema


bp = Blueprint('register', __name__)
token_whitelist = {}


@bp.route('/api/register', methods=['POST'], endpoint='register_user')
@schema_required(schema)
def register_user():
    request_json_body = request.get_json()
    name = request_json_body['name']
    email = request_json_body['email']
    password = bcrypt.generate_password_hash(request_json_body['password']).decode('utf8')

    added_user = User(name, email, password)
    profile_added = UserProfile()
    added_user.profile.append(profile_added)

    try:
        db.session.add(added_user)
        db.session.commit()
    except exc.IntegrityError:
        db.session().rollback()
        raise BadRequest("Invalid: the username or email already exist!")

    confirmation_token = generate_confirmation_token(added_user.id, added_user.email)
    global token_whitelist
    token_whitelist[confirmation_token] = 1
    send_confirmation_email(added_user.email, confirmation_token)

    return jsonify(message='Thanks for registering! Please check your email to confirm your email address.',
                   added_user=added_user.serialize, confirmation_token=confirmation_token.decode('utf-8'))


@bp.route('/api/register/confirm/<token>', methods=['GET'])
def confirm_email(token):
    global token_whitelist

    if token.encode('utf-8') not in token_whitelist:
        raise BadRequest('Account already confirmed. Please login.')

    try:
        email = jwt.decode(token, os.getenv('JWT_SECRET_KEY'), algorithms=['HS256'])['email']
        id = jwt.decode(token, os.getenv('JWT_SECRET_KEY'), algorithms=['HS256'])['id']
    except jwt.ExpiredSignatureError:
        raise BadRequest('The confirmation link is invalid or has expired.')

    user = User.query.get(id)
    user.activated = True
    db.session.add(user)
    db.session.commit()

    del token_whitelist[token.encode('utf-8')]
    return jsonify(message='Thank you for confirming your email address.', your_email=email)
