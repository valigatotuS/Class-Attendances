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

#------- routes --------------------------------#

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

#-----------------------------------------------#

#------login handlers---------------------------#

from app import login

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

@login.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('Unauthorized acces, sign in first!')
    return redirect("/sign-in")

#-----------------------------------------------#