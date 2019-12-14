from flask import request, jsonify, Blueprint
from werkzeug.exceptions import BadRequest
from app.models import User
from app import db, bcrypt, cache
from app.decorator import schema_required
from sqlalchemy import exc
from app.schemas import user_schema
import time


bp = Blueprint('user', __name__)


def load_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        raise BadRequest("None exist user")
    cache.set(str(user.id), user)
    return user


@bp.route('/api/user', methods=['GET'])
def get_all_user():
    users = User.query.all()

    return jsonify(users=[u.serialize for u in users])


@bp.route('/api/user/<int:id>', methods=['GET'])
def get_by_id(id):
    user = load_user(id)
    time.sleep(5)
    return jsonify(user=user.serialize)


@bp.route('/api/user', methods=['POST'], endpoint='add_user')
@schema_required(user_schema)
def add_user():
    payload = request.get_json()
    name = payload['name']
    email = payload['email']
    password = bcrypt.generate_password_hash(payload['password']).decode('utf8')

    try:
        added_user = User(name, email, password)
        db.session.add(added_user)
        db.session.commit()
    except exc.IntegrityError:
        db.session().rollback()
        raise BadRequest("Invalid: the username or email already exist!")

    return jsonify(added_user=added_user.serialize)


@bp.route('/api/user/<int:id>', methods=['PATCH'], endpoint='update_by_id')
@schema_required(user_schema)
def update_by_id(id):
    updated_user = User.query.get(id)

    if updated_user is None:
        raise BadRequest("None exist user")

    payload = request.get_json()
    name = payload['name']
    email = payload['email']
    password = bcrypt.generate_password_hash(payload['password']).decode('utf8')

    try:
        updated_user.username = name
        updated_user.email = email
        updated_user.password = password
        cache.set(str(id), updated_user)
        db.session.commit()
    except exc.IntegrityError:
        db.session().rollback()
        raise BadRequest("Invalid: the username or email already exist!")

    return jsonify(updated_user=updated_user.serialize)


@bp.route('/api/user/<int:id>', methods=['DELETE'])
def delete_by_id(id):
    deleted_user = load_user(id)

    if deleted_user is None:
        raise BadRequest("None exist user")

    cache.delete(str(id))
    db.session.delete(deleted_user)
    db.session.commit()

    return jsonify(deleted_user=deleted_user.serialize)


@bp.route('/api/user', methods=['DELETE'])
def delete_all_user():
    deleted_users = User.query.all()
    User.query.delete()
    db.session.commit()

    return jsonify(deleted_users_id=[u.id for u in deleted_users])
