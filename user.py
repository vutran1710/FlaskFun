from flask import request, jsonify, Blueprint
from werkzeug.exceptions import BadRequest
from models import User
from db import db


bp = Blueprint('user', __name__)


@bp.route('/api/user', methods=['GET'])
def get_all_user():
    users = User.query.all()

    if users is None:
        return "There are no user!"

    return jsonify(users=[u.serialize for u in users])


@bp.route('/api/user/<int: id>', methods=['GET'])
def get_by_id(id):
    users = User.query.filter_by(id=id).one()
    return jsonify(user=users.serialize)


@bp.route('/api/user', methods=['POST'])
def add_user():
    if not request.is_json:
        raise BadRequest("Invalid: content type is not json!")

    request_json_body = request.get_json()

    if 'name' not in request_json_body:
        raise BadRequest("None username!")

    if 'email' not in request_json_body:
        raise BadRequest("None email!")

    name = request_json_body['name']
    email = request_json_body['email']
    added_user = User(name, email)
    db.session.add(added_user)
    db.session.commit()

    return jsonify(added_user=added_user.serialize)


@bp.route('/api/user<int: id>', methods=['PATCH'])
def update_by_id(id):
    request_json_body = request.get_json()

    if not request.is_json:
        raise BadRequest("Invalid: content type is not json!")

    if "name" not in request_json_body:
        raise BadRequest("Request body does have key named name!")

    if "email" not in request_json_body:
        raise BadRequest("Request body does have key named email!")

    updated_user = User.query.filter_by(id=id).one()

    if updated_user is None:
        raise BadRequest("None exist user")

    updated_user["name"] = request_json_body["name"]
    updated_user["email"] = request_json_body["email"]
    db.session.commit()

    return jsonify(updated_user=updated_user.serialize)


@bp.route('/api/user<int: id>', methods=['DELETE'])
def delete_by_id():
    deleted_user = User.query.filter_by(id=id).one()

    if deleted_user is None:
        raise BadRequest("None exist user")

    db.session.delete(deleted_user)
    db.session.commit()

    return jsonify(deleted_user=deleted_user.serialize)
