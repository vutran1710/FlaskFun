from flask import request, jsonify, Blueprint
from werkzeug.exceptions import BadRequest
from app.models import User
from app import db
from cerberus import Validator
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
}

validator = Validator(schema)
bp = Blueprint('user', __name__)


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


@bp.route('/api/user', methods=['POST'])
def add_user():
    if not request.is_json:
        raise BadRequest("Invalid: content type is not json!")

    request_json_body = request.get_json()

    if validator.validate(request_json_body) is False:
        return {"code": 400, "name": "Invalid schema", "description": validator.errors}, 400

    name = request_json_body['name']
    email = request_json_body['email']
    added_user = User(name, email)
    try:
        db.session.add(added_user)
        db.session.commit()
    except exc.IntegrityError:
        db.session().rollback()
        raise BadRequest("Invalid: the user already exists!")

    return jsonify(added_user=added_user.serialize)


@bp.route('/api/user/<int:id>', methods=['PATCH'])
def update_by_id(id):
    if not request.is_json:
        raise BadRequest("Invalid: content type is not json!")

    request_json_body = request.get_json()

    if validator.validate(request_json_body) is False:
        return {"code": 400, "name": "Invalid schema", "description": validator.errors}, 400

    updated_user = User.query.filter_by(id=id).first()

    if updated_user is None:
        raise BadRequest("None exist user")

    try: 
        updated_user.username = request_json_body["name"]
        db.session.commit()
    except exc.IntegrityError:
        db.session().rollback()
        raise BadRequest("Invalid: the username already exists!")

    try:
        updated_user.email = request_json_body["email"]
        db.session.commit()
    except exc.IntegrityError:
        db.session().rollback()
        raise BadRequest("Invalid: the email already exists!")

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
