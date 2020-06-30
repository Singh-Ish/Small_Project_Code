import flask
from lapp import db


# mongo db database scheme

class user(db.Document):
    name = db.StringField(max_length=50)
    email = db.StringField(max_length=50, unique=True)
    role = db.StringField(max_length=30, default='student')
