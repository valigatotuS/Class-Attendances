from email import message
from flask import Blueprint, render_template, request, redirect, current_app, session, flash
from flask_login import login_required
from app.blueprints.classes import classes_bp
from app.blueprints.classes import forms
from app.database import queries

@classes_bp.route('/classes', methods=['GET','POST'])
@login_required
def classes():
    classes = queries.get_user_classes()
    form = forms.FilterForm(request.form)
    u_courses = [(class_.course_id, class_.course) for class_ in queries.get_user_classes()] #why does it change classes ?
    form.course.choices = u_courses
    if request.method == 'POST' and form.validate():
        classes = queries.get_course_classes(form.course.data)
        
    return render_template("classes/classes.html.jinja", classes=classes, form=form)

@classes_bp.route('/classes/attend/<class_id>', methods=['POST'])
@login_required
def post_attendance(class_id):
    try:
        queries.add_attendance(class_id)
    except:
        flash("you are successfuly logged in")
        session["message"] = "attendance already posted"
    return redirect("/classes")