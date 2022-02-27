from app import login
from app.database.models import User

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

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

@login.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    return redirect("/home")