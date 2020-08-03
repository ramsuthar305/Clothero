import os
from os.path import join, dirname, realpath

class Config:
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SESSION_TYPE = os.environ.get('SESSION_TYPE')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    MONGO_URI = os.environ.get('MONGO_URI')
    
