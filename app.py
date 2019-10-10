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

@app.route('/addvalue', methods=['POST'])
def add_value():
    if request.method == 'POST' and request.is_json:
        RESULT.update(request.json)
        return RESULT
    else:
        return "Fail add value"


if __name__ == "__main__":
    app.run(debug=True)