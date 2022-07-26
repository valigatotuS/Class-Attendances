from email import message
from flask import Blueprint, render_template, session
from app.blueprints.home import home_bp
from flask_login import current_user, login_user, logout_user, login_required
from app.database import queries


@home_bp.route('/home')
@login_required
def home():
    return render_template('home/index.html')

@home_bp.route('/test')
def test():
    return str([str(course['name']) for course in session['user_courses'].values()])