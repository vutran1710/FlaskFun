import os
import datetime

# sever setting
SERVER_NAME = '127.0.0.1:5000'

# jwt setting
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

# flask-jwt-extended setting
JWT_BLACKLIST_ENABLED = True
JWT_BLACKLIST_TOKEN_CHECKS = 'access'
JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(seconds=300)
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

# cache setting
CACHE_TYPE = 'redis'
CACHE_DEFAULT_TIMEOUT = 300
CACHE_REDIS_HOST = 'localhost'
CACHE_REDIS_PORT = '6379'

SQLALCHEMY_TRACK_MODIFICATIONS = False
