class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5422/postgres'

class TestConfig:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5422/user_test'
    