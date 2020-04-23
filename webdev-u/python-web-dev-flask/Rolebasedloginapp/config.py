import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "This is an INSECURE secret!! DO NOT use this in production!!"

    # flask email server settings 
    MAIL_SERVER = 'smtp.sce.carleton.ca'
    MAIL_PORT = 465
    MAIL_USE_SSL =True
    MAIL_USE_TLS = False

    MAIL_USERNAME = 'ishdeepsingh@sce.carleton.ca'
    #MAIL_PASSWORD = 'Change.711'
    MAIL_DEFAULT_SENDER = 'ishdeep.711@gmail.com'


    # settings for Flask -USer 
    USER_APP_NAME = "Flask-User MongoDB App"
    USER_ENABLE_EMAIL = True      # Disable email authentication
    USER_ENABLE_USERNAME = False    # Disable username authentication
    #USER_REQUIRE_RETYPE_PASSWORD = False    # Simplify register form
    USER_EMAIL_SENDER_NAME = USER_APP_NAME
    USER_EMAIL_SENDER_EMAIL = "ishdeepsingh@sce.carleton.ca"

    # mongo db database  settings 
    MONGODB_SETTINGS = {'db': 'testapp'}
    
    
