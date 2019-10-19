from werkzeug.exceptions import HTTPException, BadRequest
from flask_api import FlaskAPI
import app.error_handlers as handler
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = FlaskAPI(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/postgres'
    db.init_app(app)
    db.app = app
    from app.models import User, University
    db.create_all()

    app.register_error_handler(HTTPException, handler._generic_exception)
    app.register_error_handler(BadRequest, handler._bad_request)

    from app.api import user
    app.register_blueprint(user.bp)

    return app
