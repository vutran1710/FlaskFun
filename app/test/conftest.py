import os
import pytest
from app import create_app, db, bcrypt, cache
from app.models import User


@pytest.fixture
def app():
    os.environ['STAGE'] = 'test'
    app = create_app()

    user0 = User("Son", "n.vanson@gmail.com", bcrypt.generate_password_hash("1234567aA").decode('utf8'))
    user1 = User("Hoan", "n.vanhoan@gmail.com",  bcrypt.generate_password_hash("1234567bB").decode('utf8'))
    user2 = User("Lam", "tunglammeta@gmail.com",  bcrypt.generate_password_hash("1234567cC").decode('utf8'))
    user3 = User("Hung", "n.vanhung@gmail.com",  bcrypt.generate_password_hash("1234567dD").decode('utf8'))
    user4 = User("Nam", "n.huynam@gmail.com",  bcrypt.generate_password_hash("1234567eE").decode('utf8'))
    user5 = User("Viet", "n.vanviet@gmail.com",  bcrypt.generate_password_hash("1234567fF").decode('utf8'))
    user2.activated = True
    user_list = [user0, user1, user2, user3, user4, user5]

    for i in range(6):
        db.session.add(user_list[i])
        db.session.commit()

    yield app

    cache.clear()
    db.session.remove()
    db.drop_all()
