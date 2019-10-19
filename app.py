from werkzeug.exceptions import HTTPException, BadRequest
from flask_api import FlaskAPI
import error_handlers as handler


def create_app(config_filename):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)

    from db import db
    from models import User, University
    db.init_app(app)
    db.app = app
    db.create_all()

    app.register_error_handler(HTTPException, handler._generic_exception)
    app.register_error_handler(BadRequest, handler._bad_request)

    import user
    app.register_blueprint(user.bp)

    return app


if __name__ == "__main__":
    app = create_app('config.py')
    app.run(debug=True)
