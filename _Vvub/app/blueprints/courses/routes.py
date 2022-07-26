from flask import Blueprint, render_template, request, redirect, current_app, session
from app.blueprints.courses import courses_bp, forms
from flask_login import current_user, login_user, logout_user, login_required
from app.database.models import User, Class, UCourse, Attendance, Course
from app.database import queries
from app.blueprints.courses.forms import CourseForm
from app import db2

@courses_bp.route('/courses', methods=['GET','POST'])
@login_required
def courses():
    courses = queries.get_user_courses() #queries.get_user_courses_v2()
    form = CourseForm(request.form)
    if request.method == 'POST' and form.validate():
        queries.add_course(form.course.data, int(form.semester.data))
    return render_template("courses/courses.html", courses=courses, session=session)

@courses_bp.route('/coursesQ', methods=['GET'])
@login_required
def coursesq():
    courses = queries.get_user_courses_v2().all()
    out = [[course.name, course.semester, course.role] for course in courses]
    return render_template("courses/courses.html.jinja", courses=courses)

@courses_bp.route('/courses/delete/<course_id>', methods=['POST'])
@login_required
def delete_course(course_id):
    queries.delete_course(course_id)
    return redirect("/courses")

