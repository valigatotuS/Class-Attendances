from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, PasswordField, validators, SelectField
from wtforms.validators import DataRequired, Length, EqualTo

class FilterForm(FlaskForm):
    """Filter-table form"""
    course = SelectField(u'Course')
    submit = SubmitField("apply")