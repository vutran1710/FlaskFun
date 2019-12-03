"""
    Values to be used during development.
    Here you might specify the URI of a database sitting on 0.0.0.0.
"""
from . import default # noqa

DEBUG = True
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@192.168.0.103:5422/postgres"
CACHE_REDIS_URL = "redis://192.168.0.103:6379"
