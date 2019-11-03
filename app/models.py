from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=True)
    user_activated = db.Column(db.Boolean, nullable=True, default=False)

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
