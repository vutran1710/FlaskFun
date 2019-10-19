from werkzeug.exceptions import HTTPException, BadRequest
from flask_api import FlaskAPI
import app.error_handlers as handler
from flask_sqlalchemy import SQLAlchemy
from app.instance.config import Config


db = SQLAlchemy()


def create_app():
    app = FlaskAPI(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    db.app = app

    from app.models import User, University
    db.create_all()

    app.register_error_handler(HTTPException, handler._generic_exception)
    app.register_error_handler(BadRequest, handler._bad_request)

    from app.api import user, simple_data
    app.register_blueprint(user.bp)
    app.register_blueprint(simple_data.bp)

    return app
