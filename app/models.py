from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    @property
    def serialize(self):
        return {
            'username': self.username,
            'email': self.email,
            'id': self.id,
        }

    def __repr__(self):
        return '<User %r>' % self.username


class University(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    abbrev = db.Column(db.String(10), unique=True, nullable=False)

    def __init__(self, name, abbrev):
        self.name = name
        self.abbrev = abbrev

    @property
    def serialize(self):
        return {
            'name': self.name,
            'abbrev': self.abbrev,
            'id': self.id,
        }

    def __repr__(self):
        return '<User %r>' % self.name
