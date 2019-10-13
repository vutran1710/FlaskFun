from flask_api import FlaskAPI 
from flask import request, abort


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
    
    if not key:
        abort(404)
    
    if key not in RESULT:
         abort(404)
           
    return "value: %s " % (RESULT[key])  

@app.errorhandler(404) 
def not_found(error):
    return "Key does not exist.",404
  

if __name__ == "__main__":
    app.run(debug=True)