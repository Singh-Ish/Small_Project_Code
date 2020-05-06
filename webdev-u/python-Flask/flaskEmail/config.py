import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "secret_string"

    MAIL_SERVER = 'smtp.sce.carleton.ca'
    MAIL_PORT = 465
    MAIL_USE_SSL =True
    MAIL_USE_TLS = False

    MAIL_USERNAME = 'ishdeepsingh@sce.carleton.ca'
    MAIL_PASSWORD = 'Change.711'
    #MAIL_DEFAULT_SENDER = 'ishdeep.711@gmail.com'
