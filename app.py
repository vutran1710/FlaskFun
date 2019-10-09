from flask_api import FlaskAPI

app = FlaskAPI(__name__)


if __name__ == "__main__":
    app.run(debug=True)
