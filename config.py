import os

class Config(object):
    SECRET_KEY = 'expoartweb-arquitectura'
    UPLOAD_FOLDER = 'static\images'

class DevelopmentConfig(Config):
    DEBUG = True