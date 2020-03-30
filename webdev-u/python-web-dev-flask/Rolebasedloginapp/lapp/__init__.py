
from flask_mail import Mail, Message
from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine
from flask_admin import Admin 

from flask_user import login_required, UserManager, UserMixin



app=Flask(__name__)

app.config.from_object(Config)

# Setup Flask-MongoEngine
db = MongoEngine(app)

admin = Admin(app)

#adding the view to the admin 

#admin.add_view(ModelView(User,db.session))

mail = Mail(app)

from lapp.models import User 
user_manager = UserManager(app, db, User)


from lapp import routes
