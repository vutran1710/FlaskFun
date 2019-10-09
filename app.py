from flask_api import FlaskAPI 
from flask import request

app = FlaskAPI(__name__)

RESULT = {
        's1' : 'value1',
        's2' : 'value2',
        's3' : 'value3',
        's4' : 'value4',
        's5' : 'value5'
}
#  quesion 1 finshed  
@app.route('/data', methods=['GET'])
def query_string():
    args = request.args['key']       
    return RESULT[args]

#  quesion 2 finshed 
  
if __name__ == "__main__":
    app.run(debug=True)