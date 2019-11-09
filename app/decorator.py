from flask import request
from werkzeug.exceptions import BadRequest
from app import db
from app import bcrypt
from app.validator.extended import ValidatorExtended
from sqlalchemy import exc
from app.user_schema import schema

validator = ValidatorExtended(schema)


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
