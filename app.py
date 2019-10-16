from flask_api import FlaskAPI
from flask import request
from flask import jsonify
from flask import json
from werkzeug.exceptions import HTTPException, BadRequest


# bind variable db to mydatabase2
app = FlaskAPI(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/mydatabase2'


RESULT = {
    'language': 'Python',
    'framework': 'Flask',
    'website': 'Facebook',
    'editor': 'vscode'
}


@app.errorhandler(HTTPException)
def handle_exception(e):
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


@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return jsonify({
        "code": e.code,
        "name": e.name,
        "description": e.description}), 400


@app.route('/', methods=['GET'])
def get_value():
    key = request.args.get('key')

    if not key:
        raise BadRequest("You forgot key!")

    if key not in RESULT:
        raise BadRequest("Key does not exist")

    return "value: %s " % (RESULT[key])


@app.route('/data', methods=['PUT'])
def add_default_keys():
    keys_added = []

    if not request.args:
        raise BadRequest("You forgot key!")

    for param, key in request.args.items():
        if not key:
            raise BadRequest("You forgot key!")

        if key in RESULT:
            raise BadRequest("Key does exist")

        RESULT.update({key: ""})
        keys_added.append(key)

    joined_string = ', '.join(keys_added)
    response = "New keys with empty "\
        "string values added: {}".format(joined_string)

    return response


@app.route('/data', methods=['POST'])
def add_keys():
    if not request.is_json:
        raise BadRequest("Invalid: content type is not json")

    request_json_body = request.get_json()

    keys_added = []

    for key, value in request_json_body.items():
        if not key:
            raise BadRequest("Key is empty")

        if key in RESULT:
            raise BadRequest("Key does exist")

        keys_added.append(key)

    RESULT.update(request_json_body)
    joined_string = ', '.join(keys_added)
    response = 'New keys added: {}'.format(joined_string)

    return response


@app.route('/data', methods=['PATCH'])
def update_key():
    key = request.args.get('key')
    request_json_body = request.get_json()

    if key not in RESULT:
        raise BadRequest("Key does not exist")

    if not request.is_json:
        raise BadRequest("Invalid: content type is not json")

    if "value" not in request_json_body:
        raise BadRequest("request body does have key named value!")

    old_value = RESULT[key]
    new_value = request_json_body['value']
    RESULT.update({key: new_value})

    return "key {} has successful updated " \
           "from old value: {} " \
           "to new value: {}".format(key, old_value, new_value)


@app.route('/data', methods=['DELETE'])
def delete_key():
    key = request.args.get('key')

    if not key:
        raise BadRequest("You forgot key")

    if key not in RESULT:
        raise BadRequest("key does not exist")

    del RESULT[key]

    return "key: {} has been deleted!".format(key)


if __name__ == "__main__":
    app.run(debug=True)
