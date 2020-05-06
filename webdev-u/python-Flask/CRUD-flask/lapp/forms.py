from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from lapp.models import user

class userForm(FlaskForm):
    Name =  StringField("name")
    Email = StringField("email", validators=[DataRequired(), Email()])
    Role = StringField("role")