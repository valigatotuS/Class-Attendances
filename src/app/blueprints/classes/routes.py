from email import message
from flask import Blueprint, render_template, request, redirect, current_app, session, flash
from flask_login import login_required
from app.blueprints.classes import classes_bp
from app.blueprints.classes import forms
from app.database import queries

@classes_bp.route('/classes', methods=['GET'])
@login_required
def classes():
    classes = list(queries.get_user_classes())
    return render_template("classes/classes.html", classes=classes)

@classes_bp.route('/class/<class_id>/attend', methods=['GET'])
@login_required
def post_attendance(class_id):
    try:
        queries.add_attendance(class_id)
        flash("Aanwezigheid is gepost!")
    except Exception as e:
        flash("Aanwezigheid is al gepost of over uur")
    return redirect("/home")