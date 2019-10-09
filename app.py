from flask_api import FlaskAPI 
from flask import jsonify

app = FlaskAPI(__name__)

students = [{'name' : 'hung'}, 
        {'name' : 'phong'}, 
        {'name' : 'mai'},
        {'name' : 'chi'},
        {'name' : 'long'}
        ]
#  quesion 1 finshed                



	
  
    
if __name__ == "__main__":
    app.run(debug=True)