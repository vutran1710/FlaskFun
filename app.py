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

@app.route('/students/<string:name>', methods=['GET'])
def OneStudent(name):
	name_students = [student for student in students  if student['name'] == name]
	return jsonify({'student' : name_students[0]})
#  quesion 2 finshed 
  
if __name__ == "__main__":
    app.run(debug=True)