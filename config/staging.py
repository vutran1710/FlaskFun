"""
    Depending on your deployment process,
    you may have a staging step
    where you test changes to your application on a server
    that simulates a production environment.
    You’ll probably use a different database, and you may want to
    alter other configuration values for staging applications.
"""
TESTING = True
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5412/postgres"
