from flask import Flask
from flask_login import LoginManager
from app.database.database import create_db
from flask_sqlalchemy import SQLAlchemy
from app.database.models import Course
from flask_migrate import Migrate
# from app.database.models import db as db2

db = create_db(paths={"database":"app/database/db.sqlite", "init": "app/database/init_db.txt", "tables":  "app/database/rows/"}, init=True)
db2 = SQLAlchemy()
login = LoginManager()

def create_app(CONFIG):
   app = Flask(__name__)    
   app.config.from_object(CONFIG)
   migrate = Migrate(app, db)

   with app.app_context():
      login.init_app(app)
      db2.init_app(app)
      db2.create_all()
      #init_tables()
      
   #login.init_app(app)

   from app.home import home_bp
   app.register_blueprint(home_bp)

   from app.login import login_bp
   app.register_blueprint(login_bp)

   from app.classes import classes_bp
   app.register_blueprint(classes_bp)

   from app.courses import courses_bp
   app.register_blueprint(courses_bp) 

   return app


def init_tables():
   from app.database.models import User, UCourse, Class

   # u = User(
      #       fname="valentin", 
      #       lname="quevy",
      #       email="vq@gmail.com", 
      #       password_hash="vq")
      # db2.session.add(u)
      # db2.session.commit()

      # uc = UCourse(course_id=1, user_id=1, role='admin')
      # db2.session.add(uc)
      # db2.session.commit()
   
   # c = Course(name="Electronics", semester=1)
   # db2.session.add(c)
   # db2.session.commit()

   # cl = Class(
   #    id = 1,
   #    course_id = 1,
   #    date = "28/01/15",
   #    time = "13:00",
   #    duration = "120",
   #    location = "D.0.5",
   #    info = "HOC"
   # )
   # db2.session.add(cl)
   # db2.session.commit()
   
   # u = db2.session.get(User, 3)
   # db2.session.delete(u)
   # db2.session.commit()
