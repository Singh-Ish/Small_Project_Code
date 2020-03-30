from lapp import db
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_user import login_required, UserManager, UserMixin

 # Define the User document.
# NB: Make sure to add flask_user UserMixin !!!


class User(db.Document, UserMixin):
    active = db.BooleanField(default=True)

    # User authentication information
    username = db.StringField(unique=True)
    #email = db.StringField(unique=True)
    #email_confirmed_at = db.DateTime()
    password = db.StringField()

    # User information
    first_name = db.StringField()
    last_name = db.StringField()

    # unique ID 
    #studentId = db.IntField(unique=True)

    # Relationships
    roles = db.ListField(db.StringField(), default=[''])



