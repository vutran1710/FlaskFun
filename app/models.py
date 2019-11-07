from app import db
from app import bcrypt
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    _password = db.Column(db.String(300), nullable=False)
    activated = db.Column(db.Boolean, nullable=True, default=False)
    profile = db.relationship("UserProfile", backref=db.backref("user", uselist=False), passive_deletes=True)

    def __init__(self, username, email, plaintext_password):
        self.username = username
        self.email = email
        self.password = plaintext_password

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, plaintext_password):
        self._password = bcrypt.generate_password_hash(plaintext_password).decode('utf8')

    @hybrid_method
    def is_correct_password(self, plaintext_password):
        return bcrypt.check_password_hash(self.password, plaintext_password)

    @property
    def serialize(self):
        return {
            'username': self.username,
            'email': self.email,
            'password': self._password,
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
