from flask_api import FlaskAPI 
from flask import request

app = FlaskAPI(__name__)

RESULT = {
    'language' : 'Python',
    'framework' : 'Flask',
    'website' : 'Facebook',
    'editor' : 'vscode'        
}

@app.route('/', methods=['GET'])
def get_value():
    key = request.args.get('key')
    
    if not key :
        return "You forgot key"

    return "value: %s " % (RESULT[key])

@app.route('/data', methods=['POST'])
def add_value():
    request_json_body = request.get_json()

    if not request.is_json:
        return "Invalid: content type is not json"

    if not request_json_body:
        return "Request body does have key named value"
    
    new_value = request_json_body
    RESULT.update(request_json_body)
    return "value {} has successful added".format(new_value) 


if __name__ == "__main__":
    app.run(debug=True)