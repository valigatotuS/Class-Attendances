from flask import Blueprint, render_template, request, redirect, current_app
from app.courses import courses_bp, forms
from flask_login import current_user, login_user, logout_user, login_required
from app.database.models import User, Class, UCourse, Attendance, Course
from app.database import queries
from app.courses.forms import CourseForm
from app import db2

@courses_bp.route('/courses', methods=['GET','POST'])
@login_required
def courses():
    courses = queries.get_user_courses() #queries.get_user_courses_v2()
    form = CourseForm(request.form)
    if request.method == 'POST' and form.validate():
        fields = [form.course.data, int(form.semester.data)]
        queries.add_course(*fields, db=db2)
    return render_template("courses/courses.html.jinja", courses=courses, form=form)

@courses_bp.route('/coursesQ', methods=['GET','POST'])
def coursesq():
    courses = queries.get_user_courses_v2().all()
    out = [[course.name, course.semester, course.role] for course in courses]
    return render_template("courses/courses.html.jinja", courses=courses)

@courses_bp.route('/courses/add', methods=['GET','POST'])
def add_course():
    # from app import db2
    # queries.add_course("Statistiek", 2, db2)
    return redirect("/courses")