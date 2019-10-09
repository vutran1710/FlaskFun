from flask_api import FlaskAPI 

app = FlaskAPI(__name__)

my_class = {
        's1' : 'quoc',
        's2' : 'phong',
        's4' : 'long',
        's4' : 'viet',
        's5' : 'phuong'
}
#  quesion 1 finshed  
@app.route('/', methods=['GET'])
def ALlStudent():
        return my_class             

@app.route('/s1', methods=['GET'])
def student_1():
        return my_class['s1']

@app.route('/s2', methods=['GET'])
def student_2():
        return my_class['s2']

       
                
    
#  quesion 2 finshed 
  
if __name__ == "__main__":
    app.run(debug=True)