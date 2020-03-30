from flask import Flask
from config import Config
from flask_mail import Mail, Message



app=Flask(__name__)

app.config.from_object(Config)


mail = Mail(app)



from lapp import routes
