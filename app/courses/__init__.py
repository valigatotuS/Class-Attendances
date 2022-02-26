from flask import Blueprint

courses_bp = Blueprint('courses', __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path='/courses/static'
    )

from app.courses import routes