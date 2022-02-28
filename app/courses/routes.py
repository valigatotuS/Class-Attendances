from flask import Blueprint, render_template, request, redirect, current_app
from app.courses import courses_bp
from flask_login import current_user, login_user, logout_user, login_required
from app.database.models import User, Class, UCourse, Attendance, Course



@courses_bp.route('/courses', methods=['GET','POST'])
@login_required
def courses():
    id = current_user.get_id()
    ucs = UCourse.query.filter_by(user_id=id).all()
    courses_id = [uc.course_id for uc in ucs]
    courses = Course.query.filter(Course.id.in_(courses_id)).all()
    names = [course.name for course in courses]
    output = names

    return render_template("courses/courses.html.jinja", courses=courses) #str(names)
    