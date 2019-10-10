from flask_api import FlaskAPI

app = FlaskAPI(__name__)

@app.route('/data', methods=['PATCH'])
def data():
    req = request.get_json()
    RESULT.update(req)

    return "Successful updated!"

if __name__ == "__main__":
    app.run(debug=True)