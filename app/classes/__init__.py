from flask import Blueprint

classes_bp = Blueprint('classes', __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path='/classes/static'
    )

from app.classes import routes