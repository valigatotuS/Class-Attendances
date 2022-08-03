from flask import Blueprint

classes_bp = Blueprint(
    'classes',
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path='/blueprints/classes/static'
    )

from app.blueprints.classes import routes