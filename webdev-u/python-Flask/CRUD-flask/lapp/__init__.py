from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine



app=Flask(__name__)

if __name__ == "__main__":
    app.run()

app.config.from_object(Config)

db = MongoEngine()

db.init_app(app)

from lapp import routes
