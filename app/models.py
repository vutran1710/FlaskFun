from app import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=True)
    user_profile = db.relationship("UserProfile", backref=db.backref("user", uselist=False), passive_deletes=True)

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


class UserProfile(db.Model):
    __tablename__ = 'user_profile'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', onupdate="CASCADE", ondelete="CASCADE"))

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def serialize(self):
        return {
            'name': self.name,
            'age': self.age,
            'id': self.id,
        }

    def __repr__(self):
        return '<User %r>' % self.name


class University(db.Model):
    __tablename__ = 'university'
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
        return '<University %r>' % self.name
