from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False)
    activated = db.Column(db.Boolean, nullable=True, default=False)
    profile = db.relationship("UserProfile", backref=db.backref("user", uselist=False), passive_deletes=True)

    def __init__(self, username, email, password):
            self.username = username
            self.email = email
            self.password = password

    @property
    def serialize(self):
        return {
            'username': self.username,
            'email': self.email,
            'password': self.password,
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

    @property
    def serialize(self):
        return {
            'name': self.name,
            'age': self.age,
            'id': self.id,
        }

    def __repr__(self):
        return '<User %r>' % self.name
