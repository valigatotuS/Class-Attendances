from flask import Blueprint, render_template, request, redirect, current_app, session
from flask_login import login_required
from app.classes import classes_bp
from app.database import queries

@classes_bp.route('/classes', methods=['GET','POST'])
@login_required
def classes():
    classes = queries.get_user_classes()
    return render_template("classes/classes.html.jinja", classes=classes)

@classes_bp.route('/classes/attend/<class_id>')
@login_required
def post_attendance(class_id):
    queries.add_attendance(class_id)
    return redirect("/classes")