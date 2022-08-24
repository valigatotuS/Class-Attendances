from flask import session
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

def get_user_info():
    querie = f"""
        SELECT id, fname, lname, email
        FROM User u
        WHERE u.id={current_user.get_id()};"""
    user_info = db2.session.execute(querie)
    return dict(user_info.fetchone())

def get_all_courses():
    querie = """
        SELECT c.id, c.name, c.semester 
        FROM Course as c
        ORDER BY c.name ASC;"""
    courses = db2.session.execute(querie)
    return courses.fetchall()

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
        WHERE u.id={current_user.get_id()}
        ORDER BY c.name ASC;"""
    courses = db2.session.execute(querie)
    courses_dict = {course.id : dict(course) for  course in courses.fetchall()}
    return courses_dict

def get_user_classes():
    querie = f"""
        SELECT date, name as course, info, time, duration, location, cl.id, c.id as course_id
        FROM User u
        INNER JOIN UCourse uc ON u.id=uc.user_id
        INNER JOIN Course c ON uc.course_id=c.id
        INNER JOIN Class cl ON c.id=cl.course_id
        WHERE u.id={current_user.get_id()}
        ORDER BY cl.date ASC, cl.time ASC;"""
    classes = db2.session.execute(querie)
    return classes.fetchall()

def get_date_classes(date):
    querie = f"""
        SELECT date, name as course, info, time, duration, location, cl.id, c.id as course_id
        FROM User u
        INNER JOIN UCourse uc ON u.id=uc.user_id
        INNER JOIN Course c ON uc.course_id=c.id
        INNER JOIN Class cl ON c.id=cl.course_id
        WHERE u.id={current_user.get_id()} AND cl.date='{date}'
        ORDER BY cl.time ASC;"""
    classes = db2.session.execute(querie)
    return classes.fetchall()

def get_class_attendances(class_id):
    querie = f"""
        SELECT u.fname, u.lname 
        FROM Attendance att
        INNER JOIN User u ON u.id=att.user_id
        INNER JOIN Class cl ON cl.id=att.class_id
        WHERE cl.id={class_id}
        ORDER BY u.lname ASC;"""
    attendances = db2.session.execute(querie)
    return attendances.fetchall()

def get_class_absences(class_id):
    querie = f"""
        SELECT u.fname, u.lname 
        FROM Class cl
        INNER JOIN Course c ON c.id=cl.course_id
        INNER JOIN UCourse uc ON c.id=uc.course_id 
        INNER JOIN User u ON u.id=uc.user_id
        LEFT JOIN Attendance att on att.user_id=u.id
        WHERE cl.id={class_id} AND att.user_id IS NULL
        ORDER BY u.lname ASC;"""
    absences = db2.session.execute(querie) # AND uc.role!='docent' AND uc.role!='admin'
    return absences.fetchall()

def get_course_classes(id):
    querie = f"""
        SELECT date, name as course, info, time, duration, location, cl.id
        FROM Course c
        INNER JOIN Class cl ON c.id=cl.course_id
        WHERE c.id={id};"""
    classes = db2.session.execute(querie)
    return classes.fetchall()

def get_user_roles(user_id:int):
    querie = f"""
        SELECT role 
        FROM User u
        INNER JOIN UCourse uc ON u.id=uc.user_id
        WHERE u.id={user_id}"""
    uc = db2.session.execute(querie)
    roles = [userc.role for userc in uc]
    return roles

def get_course_users(course_id:int):
    querie = f"""
        SELECT u.id, u.fname, u.lname, u.email, uc.role
        FROM UCourse uc
        INNER JOIN User u ON uc.user_id=u.id
        WHERE uc.course_id={course_id}
        ORDER BY u.lname ASC, u.fname ASC;"""
    users = db2.session.execute(querie)
    return users.fetchall()

def get_course_info(course_id):
    querie = f"""
        SELECT id, name, semester
        FROM Course c
        WHERE c.id={course_id};"""
    course = db2.session.execute(querie)
    return course.fetchone()

#----post queries----#

def add_course(name, semester):
    c = Course(name=name, semester=semester)
    db2.session.add(c)
    db2.session.commit()

def add_course_class(course_id, date, time, duration, location, info):
    cl = Class(course_id=course_id, date=date, time=time, duration=duration, location=location, info=info)
    db2.session.add(cl)
    db2.session.commit()

def add_user_course(course_id, user_id, role):
    uc = UCourse(course_id=course_id, user_id=user_id, role=role)
    db2.session.add(uc)
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
    Class.query.filter_by(course_id=course_id).delete()
    UCourse.query.filter_by(course_id=course_id).delete()

    # querie = f"""
    #         DELETE 
    #         FROM Attendance as att
    #         WHERE EXISTS
    #             (SELECT u.fname, u.lname 
    #             FROM Attendance att
    #             INNER JOIN User u ON u.id=att.user_id
    #             INNER JOIN Class cl ON cl.id=att.class_id
    #             WHERE cl.course_id={course_id});"""
    # db2.session.execute(querie)
    
    db2.session.delete(course)
    db2.session.commit()

def delete_course_class(class_id):
    cclass = Class.query.get(class_id)
    db2.session.delete(cclass)
    db2.session.commit()

def delete_user_course(course_id, user_id):
    querie = f"""
        DELETE
        FROM UCourse as uc
        WHERE uc.course_id={course_id} AND uc.user_id={user_id};"""
    db2.session.execute(querie)
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

def load_user_data():
    session['user_info'] = get_user_info()
    session['user_courses'] = get_user_courses_v2()

#----------------------#

#-------sql injection--#

def sql_inj_1():
    querie = "SELECT * FROM User WHERE fname = 'john' OR 'a'='a';-- AND password = '';"
    user = db2.session.execute(querie)
    return user.fetchall()
    
#----------------------#

