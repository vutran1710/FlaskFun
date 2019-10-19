from flask import json, jsonify


def _generic_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


def _bad_request(e):
    print('bad request exception raised...')
    return jsonify({
        "code": e.code,
        "name": e.name,
        "description": e.description}), 400
