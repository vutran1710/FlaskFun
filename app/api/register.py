from flask import request, jsonify, Blueprint
from werkzeug.exceptions import BadRequest
from app.models import User, UserProfile
from app import db
from app.validator.extended import ValidatorExtended
from sqlalchemy import exc

schema = {
    'email': {
        'type':        'string',
        'required':    True,
        'empty':       False,
        'maxlength':   128
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

    added_user = User(username, email, password)
    profile_added = UserProfile()
    added_user.profile.append(profile_added)
    try:
        db.session.add(added_user)
        db.session.commit()
        return 'Thanks for registering!  Please check your email to confirm your email address.'
    except exc.IntegrityError:
        db.session().rollback()
        raise BadRequest("Invalid: the user already exists!")

    return jsonify(added_user=added_user.serialize)
