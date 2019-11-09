from flask import request, jsonify, Blueprint
from werkzeug.exceptions import BadRequest
from app.models import User
from app import db
from app import bcrypt
from app.validator.extended import ValidatorExtended
from sqlalchemy import exc

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
        'valid_password': True
    }
}

validator = ValidatorExtended(schema)
bp = Blueprint('user', __name__)


def schema_required(func):
    def wrapper(*args, **kwargs):
        if not request.is_json:
            raise BadRequest("Invalid: content type is not json!")

        request_json_body = request.get_json()

        if validator.validate(request_json_body) is False:
            raise BadRequest(validator.errors)

        name = request_json_body['name']
        email = request_json_body['email']
        password = bcrypt.generate_password_hash(request_json_body['password']).decode('utf8')
        try:
            new_user = func(name, email, password, *args, **kwargs)
        except exc.IntegrityError:
            db.session().rollback()
            raise BadRequest("Invalid: the username or email already exist!")

        return new_user

    return wrapper


@bp.route('/api/user', methods=['GET'])
def get_all_user():
    users = User.query.all()

    return jsonify(users=[u.serialize for u in users])


@bp.route('/api/user/<int:id>', methods=['GET'])
def get_by_id(id):
    users = User.query.filter_by(id=id).first()

    if users is None:
        raise BadRequest("None exist user")

    return jsonify(user=users.serialize)


@bp.route('/api/user', methods=['POST'], endpoint='add_user')
@schema_required
def add_user(name, email, password):
    added_user = User(name, email, password)
    print(added_user.serialize)
    db.session.add(added_user)
    db.session.commit()

    return jsonify(added_user=added_user.serialize)


@bp.route('/api/user/<int:id>', methods=['PATCH'], endpoint='update_by_id')
@schema_required
def update_by_id(name, email, password, id):
    updated_user = User.query.filter_by(id=id).first()

    if updated_user is None:
        raise BadRequest("None exist user")

    updated_user.username = name
    updated_user.email = email
    updated_user.password = password
    db.session.commit()

    return jsonify(updated_user=updated_user.serialize)


@bp.route('/api/user/<int:id>', methods=['DELETE'])
def delete_by_id(id):
    deleted_user = User.query.filter_by(id=id).first()

    if deleted_user is None:
        raise BadRequest("None exist user")

    db.session.delete(deleted_user)
    db.session.commit()

    return jsonify(deleted_user=deleted_user.serialize)


@bp.route('/api/user', methods=['DELETE'])
def delete_all_user():
    deleted_users = User.query.all()
    User.query.delete()
    db.session.commit()

    return jsonify(deleted_users_id=[u.id for u in deleted_users])
