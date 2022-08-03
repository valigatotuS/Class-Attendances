from flask import Blueprint

courses_bp = Blueprint('courses', __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path='/blueprints/courses/static'
    )

from app.blueprints.courses import routes