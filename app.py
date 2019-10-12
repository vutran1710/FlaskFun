from flask_api import FlaskAPI
from flask import request
from werkzeug.exceptions import HTTPException
from flask import json


app = FlaskAPI(__name__)

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


@app.route('/', methods=['GET'])
def get_value():
    key = request.args.get('key')

    if not key:
        raise HTTPException()

    if key not in RESULT:
        return "Key does not exist"

    return "value: %s " % (RESULT[key])


if __name__ == "__main__":
    app.run(debug=True)
