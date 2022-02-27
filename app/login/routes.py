from flask import Blueprint, render_template, request, redirect, current_app, url_for, session
from app.login import login_bp, queries
from app.login.forms import LoginForm, RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash
from app import db#, login 
from app.database.models import User, UCourse
from app.database.models import db as db2
from flask_login import current_user, login_user, logout_user, login_required

@login_bp.route('/sign-in', methods=['GET','POST'])
def sign_in():
    form = LoginForm(request.form)

    if current_user.is_authenticated:
            return(redirect('/logout'))
    #checking login-fields validity
    if request.method == 'POST' and form.validate():
        user = queries.get_user_info_bymail(db, form.email.data)
        user_ = User.query.filter_by(email=form.email.data).first()
        if user==None:
            return "this user do not exist"
        if check_password_hash(user["password_hash"], form.password.data):
            login_user(user_) 
            if current_user.is_authenticated:
                session['message'] = "authenticated"
                return redirect(url_for("home.about"))
            return "succesful login " + user_.fname
        else:
            return str(db.Execute("SELECT * FROM User;"))

    return render_template('login/sign-in.html.jinja', form=form)

@login_bp.route('/sign-up', methods=['GET','POST'])
def sign_up():
    form = RegisterForm(request.form)

    #adding account to the database 
    if request.method == 'POST' and form.validate():
        fields = [[form.firstname.data, form.lastname.data, form.email.data, generate_password_hash(form.password.data)]]
        queries.post_user(db, fields)
        output = db.Execute("SELECT * FROM User;")
        u = User(
            fname=form.firstname.data, 
            lname=form.lastname.data,
            email=form.email.data, 
            password_hash=form.password.data)
        db2.session.add(u)
        db2.session.commit()
        return str(output)

    return render_template('login/sign-up.html.jinja', form=form)


@login_bp.route('/sql/u', methods=['GET'])
def sql_u():
    #us = User.query.filter_by(fname='jose').first() #db2.session.query(User).filter_by(firstname='kkk').first()
    us = User.query.filter_by(email="vq@gmail.com").first()
    return (" ".join([us.fname, us.lname, us.email]))

@login_bp.route('/sql/uc', methods=['GET'])
def sql_uc():
    uc = UCourse.query.filter_by(course_id=1).first() #db2.session.query(User).filter_by(firstname='kkk').first()
    return (" ".join([str(uc.course_id), str(uc.user_id), uc.role]))

@login_bp.route('/logout')
@login_required
def logout():
    logout_user()
    session.clear()
    session['message']="logged out"
    return redirect("/home")


#------login handlers------#
from app import login

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

@login.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    session['message'] = 'unauthorized acces, log-in first'
    return redirect("/home")