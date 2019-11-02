from flask import request, jsonify, Blueprint
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                jwt_required, jwt_refresh_token_required, get_jwt_identity)
from app import flask_bcrypt, jwt
from app.models import User
from werkzeug.exceptions import BadRequest
from app.validator.extended import ValidatorExtended

schema = {
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
bp = Blueprint('login', __name__)


@jwt.unauthorized_loader
def unauthorized_response(callback):
    return jsonify({
        'ok': False,
        'message': 'Missing Authorization Header'
    }), 401


@bp.route('/api/login', methods=['POST'])
def login_user():
    if not request.is_json:
        raise BadRequest("Invalid: content type is not json!")

    request_json_body = request.get_json()

    if validator.validate(request_json_body) is False:
        raise BadRequest(validator.errors)

    user = User.query.filter_by(username=request_json_body['name']).first()

    if user and (request_json_body['password'] == user.password):
        if user.email_confirmed is False:
            return "Need email confirmed"
        access_token = create_access_token(identity=request_json_body)
        refresh_token = create_refresh_token(identity=request_json_body)
        return jsonify({'ok': True, 'data': user.serialize, 'token': access_token,
                        'refresh': refresh_token}), 200
    else:
        return jsonify({'ok': False, 'message': 'invalid username or password'}), 401


@bp.route('/api/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    ''' refresh token endpoint '''
    current_user = get_jwt_identity()
    ret = {
        'token': create_access_token(identity=current_user)
    }
    return jsonify({'ok': True, 'data': ret}), 200
