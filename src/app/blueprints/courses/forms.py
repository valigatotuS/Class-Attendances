from logging import RootLogger
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, PasswordField, validators, SelectField, HiddenField
from wtforms.validators import DataRequired, Length, EqualTo

class CourseForm(FlaskForm):
    """Course form"""
    # id = IntegerField("id")
    name = StringField("course_name")
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
    date = StringField('date')
    time = StringField('time')
    duration = IntegerField("idd")
    location = StringField('location')
    info = StringField("info")
    submit_cc = SubmitField("add cc")