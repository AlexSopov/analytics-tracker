import os


basedir = os.path.abspath(os.path.dirname(__file__))


class TestConfig(object):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app_test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
