import pytest
import sys
sys.path.append('../')
# from sqlalchemy import create_engine
# from sqlalchemy_utils import database_exists, create_database, drop_database
from app import create_app, db, instance
from app.models import User, University


@pytest.fixture
def app():
    # engine = create_engine(instance.config.TestingConfig.SQLALCHEMY_TEST_DATABASE_URI)
    # create_database(engine.url)

    app = create_app(instance.config.DevelopmentConfig)
# Sai do ham create_app cung tao schema

    # app.config.from_object(instance.config.DevelopmentConfig)
    # db.init_app(app)
    # db.app = app

    # from app.models import User, University
    # db.create_all()

    # user0 = User("Son", "n.vanson@gmail.com")
    # user1 = User("Hoan", "n.vanhoan@gmail.com")
    # user2 = User("Lam", "n.tunglam@gmail.com")
    # user3 = User("Hung", "n.vanhung@gmail.com")
    # user4 = User("Nam", "n.huynam@gmail.com")
    # user5 = User("Viet", "n.vanviet@gmail.com")

    # user_list = [user0, user1, user2, user3, user4, user5]

    # for i in range(5):
    #     db.session.add(user_list[i])
    #     db.session.commit()

    # from app.api import user, simple_data
    # app.register_blueprint(user.bp)
    # app.register_blueprint(simple_data.bp)

    return app
    # db.session.remove()
    # db.drop_all()
    # drop_database(engine.url)
