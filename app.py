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

@app.route('/data', methods=['PATCH'])
def update_key():
    key = request.args.get('key')
    req = request.get_json()

    if key not in RESULT:
        return "Key does not exist"

    old_value = RESULT[key]
    new_value = req[list(req)[0]]
    RESULT[key] = new_value

    return "key {} has successful updated " \
           "from old value: {} " \
           "to new value: {}".format(key, old_value, new_value)


if __name__ == "__main__":
    app.run(debug=True)