from werkzeug.exceptions import HTTPException, BadRequest
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
import error_handlers as handler
from api import (
    user,
    simple_data
)


# INIT FLASK INSTANCE WITH EXTERNAL CONFIG
app = FlaskAPI(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

# REGISTER ERROR HANDLERS
app.register_error_handler(HTTPException, handler._generic_exception)
app.register_error_handler(BadRequest, handler._bad_request)

# REGISTER ALL API BLUEPRINTS
app.register_blueprint(simple_data.bp)


if __name__ == "__main__":
    app.run(debug=True)
