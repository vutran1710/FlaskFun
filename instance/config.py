import os

# mail setting
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True

# gmail authentication
MAIL_USERNAME = os.getenv('MAIL_USERNAME')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')

# mail accounts
MAIL_DEFAULT_SENDER = os.getenv('MAIL_USERNAME')


SQLALCHEMY_TRACK_MODIFICATIONS = False
