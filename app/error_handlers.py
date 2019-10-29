from flask import json, jsonify
from werkzeug.exceptions import HTTPException


def _generic_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response, code


def _bad_request(e):
    print('bad request exception raised...')
    return jsonify({
        "code": 400,
        "name": e.name,
        "description": e.description}), 400
