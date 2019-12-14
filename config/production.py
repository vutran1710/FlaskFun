"""
    Values to be used in production.
    Here you might specify the URI for your database server,
    as opposed to the localhost database URI used for development.
"""
from . import default # noqa

SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@192.168.0.103:5422/postgres"
CACHE_REDIS_URL = "redis://192.168.0.103:6379"
DEBUG = False
TESTING = False
