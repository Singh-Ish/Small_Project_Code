import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "secret_string"

    #database setting
    MONGODB_SETTINGS = {'db': 'testapp'}


    