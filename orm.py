from app import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

# Create database: mydatabase2 for user postgres
engine = create_engine("postgresql://postgres:postgres@localhost:5432/mydatabase2")
if not database_exists(engine.url):
    create_database(engine.url)

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    phone = db.Column(db.String(120), unique=True)

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __repr__(self):
        return 'User: {} {}'.format(self.name, self.phone)


def insert_user(name, phone):
    newuser = User(name, phone)
    db.session.add(newuser)
    db.session.commit()


def get_user(id):
    return User.query.filter_by(id=id)


def delete_user(id):
    user = User.query.filter_by(id=id)
    db.session.delete(user)
    db.session.commit()


db.create_all()
