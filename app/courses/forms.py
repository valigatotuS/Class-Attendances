from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, PasswordField, validators
from wtforms.validators import DataRequired, Length, EqualTo

class CourseForm(FlaskForm):
    """Course form"""
    id = IntegerField("id")
    course = StringField("course")
    semester = StringField("semester")
    submit = SubmitField("add")