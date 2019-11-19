from flask import request
from werkzeug.exceptions import BadRequest
from app.validator.extended import ValidatorExtended


def schema_required(schema):
    def decorator(func):
        def wrapper(*args, **kwargs):
            validator = ValidatorExtended(schema)
            if not request.is_json:
                raise BadRequest("Invalid: content type is not json!")

            request_json_body = request.get_json()

            if validator.validate(request_json_body) is False:
                raise BadRequest(validator.errors)
            response = func(*args, **kwargs)
            return response
        return wrapper
    return decorator
