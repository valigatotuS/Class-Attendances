from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, Table, Column, Integer
from app.database.database import create_db
from app.database.models import User, Class, UCourse, Attendance, Course


from app.database.models import db as db2
login = LoginManager()

def create_app(CONFIG):
   app = Flask(__name__)    
   app.config.from_object(CONFIG)

   with app.app_context():
      login.init_app(app)
      db2.init_app(app)
      db2.create_all()
      db2.session.commit()

   from app.blueprints.home import home_bp
   app.register_blueprint(home_bp)
   from app.blueprints.login import login_bp
   app.register_blueprint(login_bp)
   from app.blueprints.classes import classes_bp
   app.register_blueprint(classes_bp)
   from app.blueprints.courses import courses_bp
   app.register_blueprint(courses_bp) 

   return app