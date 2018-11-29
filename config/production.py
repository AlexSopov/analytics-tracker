import os

USER = os.environ.get('DB_USER')
PASSWORD = os.environ.get('DB_PASSWORD')
DB_NAME = os.environ.get('DB_NAME')

SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@localhost:5432/{}'.format(USER, PASSWORD, DB_NAME)