from flask import Blueprint, render_template, request, redirect, current_app
from flask_login import login_required
from app.classes import classes_bp

@classes_bp.route('/classes', methods=['GET','POST'])
@login_required
def classes():
    return render_template("classes/classes.html.jinja")