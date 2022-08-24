from email import message
from logging import RootLogger
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, PasswordField, validators, SelectField, HiddenField, TimeField
from wtforms.validators import DataRequired, Length, EqualTo, Regexp, NumberRange, Length

class CourseForm(FlaskForm):
    """Course form"""
    # id = IntegerField("id")
    name = StringField("course_name", [Length(max=20)])
    semester = SelectField(u'semester', choices=[1,2])
    submit = SubmitField("add")

class DeleteCourseForm(FlaskForm):
    """UserCourse form"""
    course_id = HiddenField("Hidden course_id")
    submit = SubmitField("Delete c")

class UserCourseForm(FlaskForm):
    """UserCourse form"""
    user_id = IntegerField("id")
    # course_id = IntegerField("id")
    role = SelectField(u'functie', choices=['student','docent','admin'])
    submit = SubmitField("add")

class DeleteUserCourseForm(FlaskForm):
    """UserCourse form"""
    course_id = HiddenField("Hidden course_id")
    user_id = HiddenField("Hidden user_id")
    submit = SubmitField("Delete uc")

class DeleteCourseClassForm(FlaskForm):
    """CourseClass form"""
    class_id = HiddenField("Hidden class_id")
    submit_del_cc = SubmitField("Delete cc")

class CourseClassForm(FlaskForm):
    """CourseClass form"""
    course_id = IntegerField("id")
    date = StringField('date', [DataRequired(), Regexp('^\d{4}\/(0[1-9]|1[012])\/(0[1-9]|[12][0-9]|3[01])$', message="invalid date format, try YYYY/MM/DD")])
    time = StringField('time', [DataRequired(), Regexp('^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$', message="invalid time format, try HH:MM")])
    duration = IntegerField("idd", [DataRequired(), NumberRange(min=1, max=1000,message="invalid duration, try 1-1000")])
    location = StringField('location', [DataRequired(), Length(max=20)])
    info = StringField("info", [DataRequired(), Length(max=20)])
    submit_cc = SubmitField("add cc")