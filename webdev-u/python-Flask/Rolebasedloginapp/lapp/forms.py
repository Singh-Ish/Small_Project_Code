from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from lapp.models import User


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = StringField("Password", validators=[
                           DataRequired(), Length(min=5, max=15)])
    rememberMe = BooleanField("Remember Me")
    submit = SubmitField("Login")


class RegisterForm(FlaskForm):
    userId = StringField("userID", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = StringField("Password", validators=[
                           DataRequired(), Length(min=5, max=15)])
    passwordConfirm = StringField("Confirm Password", validators=[
                                  DataRequired(), Length(min=5, max=15), EqualTo('password')])
    firstName = StringField("First Name", validators=[
                            DataRequired(), Length(min=2, max=55)])
    lastName = StringField("Last Name", validators=[Length(min=2, max=55)])
    submit = SubmitField("Register Now")

    def validate_email(self, email):
        user = User.objects(email=email.data).first()
        if user:
            raise ValidationError("Email is already in use. Pick another one.")

