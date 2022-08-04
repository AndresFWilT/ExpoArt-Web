import os

class Config(object):
    SECRET_KEY = 'my_secret_key'
    UPLOAD_FOLDER = 'static\images'

class DevelopmentConfig(Config):
    DEBUG = True