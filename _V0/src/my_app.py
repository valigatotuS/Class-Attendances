from flask import Flask, url_for, request, make_response, session
from flask.templating import render_template
from werkzeug.utils import redirect
from my_database import create_db
from my_queries import get_user_info_bymail, get_user_info_byid, get_user_classes, get_user_courses
from werkzeug.security import check_password_hash

def create_app(config_):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_)
        
    db_ = create_db(paths=app.config["DB_PATHS"], init = True)

    @app.route("/")
    def Home():
        return render_template('index.html')
            
    @app.route('/login',methods = ['POST', 'GET'])
    def Login():
        session.clear()
        
        if request.method == 'POST':
            (email, pw) = (request.form['email'], request.form['password'])
            user = get_user_info_bymail(db_, email)
            error = None
            if user == None: 
                error = "fail, incorrect email, try again"
            if user != None and not check_password_hash(user["password_hash"], pw): 
                error = "fail, incorrect pw, try again "
            if error!=None: 
                return error
            else:
                session['UserId'] = user['UserId']
                return redirect(url_for('Dashboard'))
        else:
            return render_template('login2.html')        
             
    @app.route("/dashboard")
    def Dashboard():
        id = session["UserId"]
        if(id != None):       
            user = {'info':         get_user_info_byid(db_, id),
                    'courses':      get_user_courses(db_, id), 
                    'classes':      get_user_classes(db_, id)}
        
            return render_template("dashboard.html", user = user)

    @app.route("/about")
    def About():
        return render_template('about.html')

    return app