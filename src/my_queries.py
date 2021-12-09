from my_database import create_db, db 
import json

def get_table(db_:db, table:str):
    q = f"SELECT * FROM {table};"
    return db_.Execute(q)

def get_user_info_byid(db_:db, userid:int):
    res = db_.Execute(f"""
        SELECT UserId, fname, lname, email
        FROM User u
        WHERE u.UserId={userid};""", as_json=True)
    if len(res)<1: res = [None] 
    return res[0]

def get_user_info_bymail(db_:db, email:str):
    res = db_.Execute(f"""
        SELECT UserId, fname, lname, email, password_hash
        FROM User u
        WHERE u.email='{email}';""", as_json=True)
    if len(res)<1: res = [None] 
    return res[0]

# def get_permissions(db_:db, course:str, role:str):
#     res = db_.Execute(f"""
#         SELECT UserId, fname, lname, email, password_hash
#         FROM User u
#         WHERE u.email='{email}';""", as_json=True)
#     if len(res)<1: res = [None] 
#     return res[0]

def get_user_classes(db_:db, userid:int):
    #info, date, time, location
    res = db_.Execute(f"""
        SELECT date, name as course, info, time, duration, location
        FROM User u
        INNER JOIN UCourse uc ON u.UserId=uc.UserId
        INNER JOIN Course c ON uc.CourseId=c.CourseId
        INNER JOIN Class cl ON c.CourseId=cl.CourseId
        WHERE u.UserId={userid};""", as_json = True)
    if len(res)<1: res = [None] 
    return res

def get_user_courses(db_:db, userid:int):
    #info, date, time, location
    res = db_.Execute(f"""
        SELECT name as course_name, semester, role
        FROM User u
        INNER JOIN UCourse uc ON u.UserId=uc.UserId
        INNER JOIN Course c ON uc.CourseId=c.CourseId
        WHERE u.UserId={userid};""", as_json = True)
    if len(res)<1: res = [None] 
    return res

def post_class_attendance(db_:db, userid:int, classid:int):
    q = f"""INSERT INTO Attendance 
        VALUES({classid},{userid});"""
    db_.Execute(q)

def post_class(db_:db, values:list):
    id_ = db_.Execute("SELECT COUNT(*) FROM Class")
    id = id_[0][0]+1
    q = f"""INSERT INTO Class 
        VALUES({id},?,?,?,?,?,?);"""
    db_.ExecuteMany(q, values)

def drop_class(db_:db, classid:int):
    q = f"""DELETE FROM Class
            WHERE ClassId = {classid}"""
    db_.Execute(q)

def get_class_attendance(db_:db, classid:int):
    q = f"""SELECT fname, lname
        FROM Attendance a
        INNER JOIN User u ON a.UserId=u.UserId
        WHERE a.ClassId={classid}"""
    return db_.Execute(q)

def post_course(db_:db, values:list):
    id_ = db_.Execute("SELECT COUNT(*) FROM Course") # getting id from last row
    id = id_[0][0]+1
    q = f"""INSERT INTO Course 
        VALUES({id},?,?);"""
    db_.ExecuteMany(q, values)

def drop_course(db_:db, courseid:int):
    q = f"""DELETE FROM Course
            WHERE CourseId = {courseid}"""
    db_.Execute(q)  

def post_usercourse(db_:db, values:list):
    q = f"""INSERT INTO UCourse 
        VALUES(?,?,?);"""
    db_.ExecuteMany(q, values)

def drop_usercourse(db_:db, courseid:int, userid:int):
    q = f"""DELETE FROM UCourse
            WHERE CourseId = {courseid} AND UserId={userid}"""
    db_.Execute(q)  

def post_user(db_:db, values:list): 
    id_ = db_.Execute("SELECT COUNT(*) FROM User") # getting id from last row
    id = id_[0][0]+1
    q = f"""INSERT INTO User 
        VALUES({id},?,?,?,?);"""
    db_.ExecuteMany(q, values)

"""Test code:"""

# a_db = create_db(init=True)
#bbb = get_user_info(a_db, 1)
#post_class(a_db, [])

#row = [5,"19/12/2021", "14:00","120","Fab-Lab","TESTTT"]
#post_class(a_db, [row])
#drop_class(a_db, 6)
#bbb = get_user_classes(a_db, 1)
#bbb = get_class_attendance(a_db, 1)
#drop_course(a_db, 10)
#post_course(a_db, [["Computersystemen","1"]])
#post_usercourse(a_db, [[1,10,"student"]])
#drop_usercourse(a_db, 10, 10)
#post_user(a_db, [["Kris","Steenhout","ks@gmail.com","ks"]])

# bbb = get_table(a_db, "UCourse")

# bbb = get_user_info_bymail(a_db, "vq@gmail.com")
# print(bbb, type(bbb))
#print(bbb['password'])
#[print(e) for e in bbb]
#print(len(a_list))