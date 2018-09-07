from os import getenv

ENV = getenv('FLASK_ENV', default='production')
DEBUG = ENV == 'development'

SECRET_KEY = getenv('SECRET_KEY')
TINYDB_PATH = getenv('TINYDB_PATH', 'repapp.db')

SQLALCHEMY_DATABASE_URI = getenv('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = getenv('SQLALCHEMY_TRACK_MODIFICATIONS')