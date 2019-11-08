"""
    Values to be used during development.
    Here you might specify the URI of a database sitting on localhost.
"""
from . import default # noqa

DEBUG = True
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5422/postgres"
