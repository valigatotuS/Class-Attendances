from email import message
from flask import Blueprint, render_template
from app.home import home_bp

@home_bp.route('/')
@home_bp.route('/home')
def home():
    return render_template('home/home_.html.jinja')