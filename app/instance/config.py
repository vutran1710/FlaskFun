class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5422/postgres'


class TestingConfig:
    SQLALCHEMY_TEST_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5422/user_test'
