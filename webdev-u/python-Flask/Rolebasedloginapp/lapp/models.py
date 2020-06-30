import flask
from lapp import db
from werkzeug.security import generate_password_hash, check_password_hash
from lapp import admin

 # Define the User document.
# NB: Make sure to add flask_user UserMixin !!!


class User(db.Document):
    # user authentication information
    userId = db.IntField(unique=True)  # same as student id
    email = db.StringField(max_length=30, unique=True)
    password = db.StringField()

    # user information
    firstName = db.StringField(max_length=50)
    lastName = db.StringField(max_length=50)
    
    # Relationships
    #roles = db.StringField(default='student')


    def set_password(self, password):
        self.password = generate_password_hash(password)

    def get_password(self, password):
        return check_password_hash(self.password, password)

    
    


#defining the role data-model
class Role(db.Document):
    userId = db.IntField(unique=True)
    rname = db.StringField(max_length=50, default = 'student')

'''
#definig the user role association table 
class UserRole(db.Document):
    email = db.StringField(max_length=50)
    rname = db.StringField(max_length=50)

    #def urole:
        #uid = User get the data from the email 
        # assiging the admin or student role to each user 

     #   if (uid.roles==''):
      ##     uid.save()

        
'''
