import os
from app.database.database import db, create_db

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    DB_PATHS = {
        "database":"app/database/db.sqlite",
        "init": "app/database/init_db.txt",
        "tables":  "app/database/records_csv/"}
    DB_RECORDS = "app/database/records_csv/"
    #DATABASE = create_db(paths=DB_PATHS, init = True)
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.abspath("./app/database/db4.sqlite")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

