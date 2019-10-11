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
def add_keys():
    request_json_body = request.get_json()

    if not request.is_json:
        return "Invalid: content type is not json"

    for key, value in request_json_body.items():
        if not key:
            return "Key is empty"

        if key in RESULT:
            return "Key does exist "
      
    RESULT.update(request_json_body)
            
    return ["Item {} is added".format(item) for item in request_json_body.items()]

@app.route('/data', methods=['PATCH'])
def update_key():
    key = request.args.get('key')
    request_json_body = request.get_json()

    if key not in RESULT:
        return "Key does not exist"

    if not request.is_json:
        return "Invalid: content type is not json"

    if "value" not in request_json_body:
        return "request body does have key named value!"

    old_value = RESULT[key]
    new_value = request_json_body['value']
    RESULT.update({ key: new_value })

    return "key {} has successful updated " \
           "from old value: {} " \
           "to new value: {}".format(key, old_value, new_value)

@app.route('/data', methods=['DELETE'])
def delete_key():
    key = request.args.get('key')

    if not key:
        return "You forgot key"
    
    if key not in RESULT:
        return "key does not exist"

    del RESULT[key]

    return "key: {} has been deleted!".format(key)

if __name__ == "__main__":
    app.run(debug=True)