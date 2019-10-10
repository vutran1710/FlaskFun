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
  

if __name__ == "__main__":
    app.run(debug=True)