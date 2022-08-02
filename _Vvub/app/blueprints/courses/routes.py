from flask import Blueprint, flash, render_template, request, redirect, current_app, session
from app.blueprints.courses import courses_bp, forms
from flask_login import current_user, login_user, logout_user, login_required
from app.database.models import User, Class, UCourse, Attendance, Course
from app.database import queries
from app.blueprints.courses.forms import CourseForm, UserCourseForm, DeleteUserCourseForm, DeleteCourseForm, DeleteCourseClassForm, CourseClassForm
from app import db2
from functools import wraps

#------- authentication decorators-----------#

def admin_required(func):
    """Admin proprietary action"""
    @wraps(func)
    def decorated_vieuw(*args, **kwargs):
        if(session['user_info']['role']=='admin'):
            return func(*args, **kwargs)
        else:
            flash("Onbevoegde toegang!")
            return redirect("/home")
    return decorated_vieuw

def admin_or_teacher_required(func):
    """Admin/teacher proprietary action"""
    @wraps(func)
    def decorated_vieuw(*args, **kwargs):
        if(session['user_info']['role'] in ['admin', 'docent']):
            return func(*args, **kwargs)
        else:
            flash("Onbevoegde toegang!")
            return redirect("/home")
    return decorated_vieuw

#-----------------------------------------------#

#------- routes --------------------------------#

@courses_bp.route('/courses', methods=['GET','POST'])
@login_required
def courses():
    courses = None
    add_course_form = CourseForm(request.form)
    del_course_form = DeleteCourseForm(request.form)
    if session['user_info']['role'] == 'admin':
        if request.method == 'POST' and add_course_form.validate():
            queries.add_course(add_course_form.name.data, int(add_course_form.semester.data))
            flash('Cursus is toegevoegd')
        elif request.method == 'POST' and del_course_form.validate():
            queries.delete_course(del_course_form.course_id.data)
            flash('Cursus is verwijderd')
        courses = queries.get_all_courses()
    else: 
        courses = session['user_courses'].values() #queries.get_user_courses() #queries.get_user_courses_v2()
    return render_template("courses/courses.html", courses=courses, course_form=add_course_form,del_course_form=del_course_form)

@courses_bp.route('/course/<course_id>/start', methods=['POST','GET'])
@login_required
def course_start_(course_id):
    course = queries.get_course_info(course_id)
    return render_template("courses/course_start.html", course=course)

@courses_bp.route('/course/<course_id>/users', methods=['POST','GET'])
@login_required
def course_users_(course_id):
    add_uc_form = UserCourseForm(request.form)
    del_uc_form = DeleteUserCourseForm(request.form)
    if request.method == 'POST':
        if add_uc_form.validate():
            queries.add_user_course(course_id, add_uc_form.user_id.data, add_uc_form.role.data)
            flash("Persoon is toegevoegd!")
        elif del_uc_form.validate():
            queries.delete_user_course(del_uc_form.course_id.data, del_uc_form.user_id.data)
            flash('Persoon is verwijderd')

    course = queries.get_course_info(course_id)
    users = queries.get_course_users(course_id)
    return render_template("courses/course_users.html", course=course, users=users, add_uc_form=add_uc_form, del_uc_form=del_uc_form)

@courses_bp.route('/course/<course_id>/classes', methods=['POST','GET'])
@login_required
def course_classes_(course_id):
    add_cc_form = CourseClassForm(request.form)
    del_cc_form = DeleteCourseClassForm(request.form)

    if add_cc_form.validate_on_submit() and add_cc_form.submit_cc.data:
        queries.add_course_class(course_id, add_cc_form.date.data, add_cc_form.time.data, add_cc_form.duration.data, add_cc_form.location.data, add_cc_form.info.data)
        flash('Les is toegevoegd')
    if del_cc_form.validate_on_submit() and del_cc_form.submit_del_cc.data:
        queries.delete_course_class(del_cc_form.class_id.data)
        flash('Les is verwijderd')

    course = queries.get_course_info(course_id)
    classes = queries.get_course_classes(course_id)
    return render_template("courses/course_classes.html", course=course, classes=classes, add_cc_form=add_cc_form, del_cc_form=del_cc_form)

@courses_bp.route('/course/<course_id>/class/<class_id>/attendances', methods=['POST','GET'])
@login_required
@admin_or_teacher_required
def course_class_attendances_(course_id, class_id):
    course = queries.get_course_info(course_id)
    class_presences = queries.get_class_attendances(class_id)
    class_absences = queries.get_class_absences(class_id)
    return render_template("courses/course_class_attendances.html", course=course, class_presences=class_presences, class_absences=class_absences)

#-----------------------------------------------#
