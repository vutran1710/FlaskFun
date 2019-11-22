from flask import request, Blueprint, jsonify
from flask_jwt_extended import (create_access_token, get_raw_jwt, jwt_required)
from werkzeug.exceptions import BadRequest
from app.models import User
from app import bcrypt, jwt_manager
from app.decorator import schema_required
from app.schemas import login_schema


bp = Blueprint('login', __name__)
blacklist = set()


@jwt_manager.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in blacklist


@jwt_manager.unauthorized_loader
def unauthorized_response(callback):
    return jsonify(message='Missing Authorization Header'), 401


@bp.route('/api/login', methods=['POST'])
@schema_required(login_schema)
def login_user():
    payload = request.get_json()
    username = payload['name']
    password = payload['password']
    user = User.query.filter_by(username=username).first()

    if user and bcrypt.check_password_hash(user.password, password):
        if user.activated is False:
            raise BadRequest("Need email confirmed.")
        access_token = create_access_token(identity=payload)
        return jsonify(user=user.serialize, message="Login success.", token=access_token)
    else:
        raise BadRequest('Invalid username or password.')


@bp.route('/api/logout', methods=['DELETE'])
@jwt_required
def logout():
    jti = get_raw_jwt()['jti']
    blacklist.add(jti)
    return jsonify(message="Successfully logged out.")
