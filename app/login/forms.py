from email import message
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators
from wtforms.validators import DataRequired, Length, EqualTo
from werkzeug.security import generate_password_hash

class LoginForm(FlaskForm):
    """Sign-in form"""
    email = StringField("email", [DataRequired(message="fill your email out")])
    password = PasswordField("password", [DataRequired(message="fill your password out")])
    submit = SubmitField("Log in")

class RegisterForm(FlaskForm):
    """Sign-up form"""
    firstname = StringField("firstname", [DataRequired()])
    lastname = StringField("lastname", [DataRequired()])
    email = StringField("email", [DataRequired()])
    password = PasswordField("password", [DataRequired()])
    submit = SubmitField("Create account")