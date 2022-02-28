from app.database.models import User
from sqlalchemy import insert

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