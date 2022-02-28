from app.database.models import User
from sqlalchemy import insert
from flask_login import current_user
from app.database.models import User, Class, UCourse, Attendance, Course
from app import db2

def post_user(db_, values:list): 
    id_ = db_.Execute("SELECT COUNT(*) FROM User") 
    id = id_[0][0]+1
    q = f"""INSERT INTO User 
        VALUES({id},?,?,?,?);"""
    db_.ExecuteMany(q, values)

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

def add_user(fname,lname,email,password_hash,db):
    u = User(
        fname=fname, 
        lname=lname,
        email=email, 
        password_hash=password_hash)
    db.session.add(u)
    db.session.commit()

def delete_records(db, Model):
    db.session.query(Model).delete()
    db.session.commit()

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