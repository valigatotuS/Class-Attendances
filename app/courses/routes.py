from flask import Blueprint, render_template, request, redirect, current_app
from app.courses import courses_bp

@courses_bp.route('/courses', methods=['GET','POST'])
def courses():
    return "courses"