from app.database.models import User
from sqlalchemy import insert
from flask_login import current_user
from app.database.models import User, Class, UCourse, Attendance, Course
from app import db2

#----select queries----#

def get_user_info_bymail(db_, email:str):
    res = db_.Execute(f"""
        SELECT UserId, fname, lname, email, password_hash
        FROM User u
        WHERE u.email='{email}';""", as_json=True)
    if len(res)<1: res = [None] 
    return res[0]

def get_user_courses():
    id = current_user.get_id()
    ucs = UCourse.query.filter_by(user_id=id).all()
    courses_id = [uc.course_id for uc in ucs]
    courses = Course.query.filter(Course.id.in_(courses_id)).all()
    return courses

def get_user_courses_v2():
    querie = f"""
        SELECT c.name, c.semester, uc.role, c.id
        FROM User u
        INNER JOIN UCourse uc ON u.id=uc.user_id
        INNER JOIN Course c ON uc.course_id=c.id
        WHERE u.id={current_user.get_id()};"""
    courses = db2.session.execute(querie)
    return courses

def get_user_classes():
    querie = f"""
        SELECT date, name as course, info, time, duration, location, cl.id, c.id as course_id
        FROM User u
        INNER JOIN UCourse uc ON u.id=uc.user_id
        INNER JOIN Course c ON uc.course_id=c.id
        INNER JOIN Class cl ON c.id=cl.course_id
        WHERE u.id={current_user.get_id()};"""
    classes = db2.session.execute(querie)
    return classes

def get_course_classes(id):
    querie = f"""
        SELECT date, name as course, info, time, duration, location, cl.id
        FROM User u
        INNER JOIN UCourse uc ON u.id=uc.user_id
        INNER JOIN Course c ON uc.course_id=c.id
        INNER JOIN Class cl ON c.id=cl.course_id
        WHERE c.id={id} AND u.id={current_user.get_id()};"""
    classes = db2.session.execute(querie)
    return classes

def get_user_roles(user_id:int):
    querie = f"""
        SELECT role 
        FROM User u
        INNER JOIN UCourse uc ON u.id=uc.user_id
        WHERE u.id={user_id}"""
    uc = db2.session.execute(querie)
    roles = [userc.role for userc in uc]
    return roles 

#----post queries----#

def add_course(name, semester):
    c = Course(name=name, semester=semester)
    db2.session.add(c)
    db2.session.commit()

def add_attendance(class_id):
    a = Attendance(class_id=class_id ,user_id=current_user.get_id())
    db2.session.add(a)
    db2.session.commit()

def add_user(fname,lname,email,password_hash,db):
    u = User(
        fname=fname, 
        lname=lname,
        email=email, 
        password_hash=password_hash)
    db.session.add(u)
    db.session.commit()

#----delete queries---#

def delete_records(db, Model):
    db.session.query(Model).delete()
    db.session.commit()

def delete_course(course_id):
    course = Course.query.get(course_id)
    db2.session.delete(course)
    db2.session.commit()

#----sub functions----#

def fill_table(path:str, Model, db):
    records = csv2dict(path)
    db.session.execute(insert(Model), records)
    db.session.commit()

def csv2dict(path:str):
    lines = []
    with open(path, 'r') as file:
        lines = [r.split(',') for r in [r for r in file.read().split('\n')]]
    (keys, records) = (lines[0], lines[1:-1])
    return [dict(zip(keys, record)) for record in records]