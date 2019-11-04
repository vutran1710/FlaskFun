import os
from werkzeug.exceptions import BadRequest
from flask_api import FlaskAPI
import app.error_handlers as handler
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    STAGE = os.getenv('STAGE') or 'development'
    CONFIG_PATH = os.getcwd() + '/config/' + STAGE + '.py'

    if not os.path.isfile(CONFIG_PATH):
        raise Exception('invalid stage config')

    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_pyfile(CONFIG_PATH)

    db.init_app(app)
    db.app = app

    from app.models import User # noqa
    db.create_all()

    app.register_error_handler(Exception, handler._generic_exception)
    app.register_error_handler(BadRequest, handler._bad_request)

    from app.api import user, simple_data
    app.register_blueprint(user.bp)
    app.register_blueprint(simple_data.bp)

    return app


app = create_app()
