from email import message
from flask import Blueprint, render_template
from app.blueprints.home import home_bp
from flask_login import current_user, login_user, logout_user, login_required


@home_bp.route('/home')
@login_required
def home():
    return render_template('home/index.html')