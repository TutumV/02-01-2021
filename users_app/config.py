import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    HOST = os.environ.get('HOST', '127.0.0.1')
    PORT = os.environ.get('PORT', '5000')
    DEBUG = os.environ.get('DEBUG', True)
    DB_USER = os.environ.get('DB_USER', 'postgres')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', 'password')
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_PORT = os.environ.get('DB_PORT', '5432')
    DATABASE = os.environ.get('DATABASE', 'postgres')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'super-secret')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL',
                                             f'postgres://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DATABASE}')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
