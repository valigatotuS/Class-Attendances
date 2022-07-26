from operator import index
from flask import Blueprint, render_template, request, redirect, current_app, url_for, session, flash
from app.blueprints.login import login_bp
from app.database import queries
from app.blueprints.login.forms import LoginForm, RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash
from app.database.models import User, UCourse, Attendance, Class, Course
from app.database.models import db as db2
from flask_login import current_user, login_user, logout_user, login_required
from flask import current_app as app

@login_bp.route('/sign-in', methods=['GET','POST'])
@login_bp.route('/', methods=['GET','POST'])
def sign_in():
    form = LoginForm(request.form)

    if current_user.is_authenticated:
            return(redirect('/logout'))
    #checking login-fields validity
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user == None:
            flash("No user with this email exist")
        elif   (check_password_hash(user.password_hash, form.password.data) and
                (form.role.data=="student" or form.role.data in queries.get_user_roles(user.id))):  
            login_user(user) 
            queries.load_user_data() # loading user data
            session['user_info']['role'] = form.role.data
            flash(f"Hello, {session['user_info']['fname']}!")
            return redirect("/home")
        else:
            flash("Incorrect password, try again!")
        return redirect("/sign-in")
    return render_template('login/signin.html', form=form)

@login_bp.route('/sign-up', methods=['GET','POST'])
def sign_up():
    form = RegisterForm(request.form)
    #adding account to the database 
    if request.method == 'POST' and form.validate():
        fields = [form.firstname.data, form.lastname.data, form.email.data, generate_password_hash(form.password.data)]
        queries.add_user(*fields, db=db2)
        flash("User is added, try to login")
        return redirect("/sign-in")
    return render_template('login/signup.html', form=form)

@login_bp.route('/logout')
@login_required
def logout():
    logout_user()
    session.clear()
    flash("Logged out")
    return redirect("/sign-in")

#------test routes-----#

@login_bp.route('/sql/u', methods=['GET'])
def sql_u():
    #us = User.query.filter_by(fname='jose').first() #db2.session.query(User).filter_by(firstname='kkk').first()
    us = User.query.filter_by(email="vq@gmail.com").first()
    
    return (" ".join([us.fname, us.lname, us.email]))

@login_bp.route('/sql/uc', methods=['GET'])
def sql_uc():
    uc = UCourse.query.filter_by(course_id=1).first() #db2.session.query(User).filter_by(firstname='kkk').first()
    return (" ".join([str(uc.course_id), str(uc.user_id), uc.role]))

@login_bp.route('/sql/test', methods=['GET'])
def sql_test():
    
    # meta = MetaData()
    # meta.create_all(db2.engine)
    # queries.delete_records(db2, User)
    # queries.fill_table(app.config["DB_RECORDS"]+User.__tablename__+".csv" , User, db2)


    # u = UCourse.query.filter_by(course_id=1).first()
    # db2.session.delete(u)
    # db2.session.commit()
    
    return str("kkk") # app.config["DB_RECORDS"]

@login_bp.route('/sql/courses', methods=['GET'])
def sql_classes():
    id = current_user.get_id()
    ucs = UCourse.query.filter_by(user_id=id).all()
    courses_id = [uc.course_id for uc in ucs]
    courses = Course.query.filter(Course.id.in_(courses_id)).all()
    names = [course.name for course in courses]
    return str(names)


#------login handlers------#

from app import login

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

@login.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('Unauthorized acces, sign in first!')
    return redirect("/sign-in")