import os
import pytest
from app import create_app, db
from app.models import User


@pytest.fixture
def app():
    os.environ['STAGE'] = 'test'
    app = create_app()

    user0 = User("Son", "n.vanson@gmail.com")
    user1 = User("Hoan", "n.vanhoan@gmail.com")
    user2 = User("Lam", "n.tunglam@gmail.com")
    user3 = User("Hung", "n.vanhung@gmail.com")
    user4 = User("Nam", "n.huynam@gmail.com")
    user5 = User("Viet", "n.vanviet@gmail.com")
    user_list = [user0, user1, user2, user3, user4, user5]

    for i in range(6):
        db.session.add(user_list[i])
        db.session.commit()

    yield app
    db.session.remove()
    db.drop_all()
