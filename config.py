import os
from app.database.database import db, create_db

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    DB_PATHS = {
        "database":"app/database/db.sqlite",
        "init": "app/database/init_db.txt",
        "tables":  "app/database/rows/"}
    DATABASE = create_db(paths=DB_PATHS, init = True)
    SQLALCHEMY_DATABASE_URI = "sqlite://///home/valigatotus/Documents/github/temp/app/database/db2.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

