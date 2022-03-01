import imp
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(64), index=True)
    lname = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    
    def __repr__(self):
        return '<User %s %s %s %s>' % (self.fname, self.lname, self.email, self.password_hash)

class UCourse(db.Model):
    __tablename__ = 'UCourse'   
    course_id = db.Column(db.Integer, db.ForeignKey("User.id"), primary_key=True)
    user_id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(120))

class Attendance(db.Model):
    __tablename__ = 'Attendance'
    class_id = db.Column(db.Integer, db.ForeignKey('Class.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), primary_key=True)

class Course(db.Model):
    __tablename__ = 'Course'
    meta = MetaData()
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    semester = db.Column(db.Integer)

class Class(db.Model):
    __tablename__ = 'Class'
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('Course.id'))
    date = db.Column(db.String(32))
    time = db.Column(db.String(32))
    duration = db.Column(db.Integer)
    location = db.Column(db.String(120))
    info = db.Column(db.String(120))