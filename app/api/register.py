from flask import request, jsonify, Blueprint
from werkzeug.exceptions import BadRequest
from app.models import User, UserProfile
from app import db
from app.validator.extended import ValidatorExtended
from sqlalchemy import exc
from app.helper.send_confirmation_email import send_confirmation_email, confirm_serializer
from datetime import datetime


schema = {
    'email': {
        'type':        'string',
        'required':    True,
        'empty':       False,
        'maxlength':   128,
        'valid_email': True
    },
    'name': {
        'type':      'string',
        'required':  True,
        'empty':     False,
        'maxlength': 128
    },
    'password': {
        'type':      'string',
        'required':  True,
        'empty':     False,
        'maxlength': 128,
        'contain_uppercase': True,
        'contain_lowercase': True,
        'minlength': 8
    }
}

validator = ValidatorExtended(schema)
bp = Blueprint('register', __name__)


@bp.route('/api/register', methods=['POST'])
def register_user():
    if not request.is_json:
        raise BadRequest("Invalid: content type is not json!")

    request_json_body = request.get_json()

    if validator.validate(request_json_body) is False:
        raise BadRequest(validator.errors)

    username = request_json_body['name']
    email = request_json_body['email']
    password = request_json_body['password']

    added_user = User(username, email)
    added_user.password = password
    user_profile_added = UserProfile()
    user_profile_added2 = UserProfile()
    added_user.user_profile.append(user_profile_added)
    added_user.user_profile.append(user_profile_added2)
    try:
        db.session.add(added_user)
        send_confirmation_email(added_user.email)
        added_user.email_confirmation_sent_on = datetime.now()
        db.session.commit()
        return 'Thanks for registering!  Please check your email to confirm your email address.'
    except exc.IntegrityError:
        db.session().rollback()
        raise BadRequest("Invalid: the user already exists!")

    return jsonify(added_user=added_user.serialize)


@bp.route('/api/register/confirm/<token>')
def confirm_email(token):
    try:
        email = confirm_serializer.loads(token, salt='email-confirmation-salt', max_age=3600)
    except:
        return 'The confirmation link is invalid or has expired.'

    user = User.query.filter_by(email=email).first()

    if user.email_confirmed:
        return 'Account already confirmed. Please login.'
    else:
        user.email_confirmed = True
        user.email_confirmed_on = datetime.now()
        db.session.add(user)
        db.session.commit()
        return 'Thank you for confirming your email address :v'
