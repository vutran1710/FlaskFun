from werkzeug.exceptions import BadRequest
from flask_api import FlaskAPI
import app.error_handlers as handler
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app(env_file):
    app = FlaskAPI(__name__, instance_relative_config=True)
    # Load the default configuration
    app.config.from_object('config.default')

    # Load the configuration from the instance folder
    app.config.from_pyfile('config.py')

    # Load the file specified by the APP_CONFIG_FILE environment variable
    # Variables defined here will override those in the default configuration
    app.config.from_envvar(env_file)

    db.init_app(app)
    db.app = app

    from app.models import User, UserProfile

    db.create_all()

    app.register_error_handler(Exception, handler._generic_exception)
    app.register_error_handler(BadRequest, handler._bad_request)

    from app.api import user, simple_data, register
    app.register_blueprint(user.bp)
    app.register_blueprint(simple_data.bp)
    app.register_blueprint(register.bp)

    return app
