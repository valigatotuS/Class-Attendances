from flask import Blueprint, render_template, request, redirect, current_app, session
from flask_login import login_required
from app.classes import classes_bp
from app.database import queries

@classes_bp.route('/classes', methods=['GET','POST'])
@login_required
def classes():
    classes_ = queries.get_user_classes()
    return render_template("classes/classes.html.jinja", classes=classes_)