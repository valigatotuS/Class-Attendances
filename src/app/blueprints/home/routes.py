from email import message
from flask import Blueprint, render_template, session, flash
from app.blueprints.home import home_bp
from flask_login import current_user, login_user, logout_user, login_required
from app.database import queries

#------- routes --------------------------------#

@home_bp.route('/home')
@login_required
def test():
    from datetime import datetime as dt
    today_date = dt.today().date().strftime('%Y/%m/%d')
    time_now = dt.today().time().strftime('%H:%M')
    todays_classes = queries.get_date_classes(today_date)
    user_classes = queries.get_user_classes()
    return render_template('home/index.html', todays_classes=todays_classes, date=dt.today().date())

#-----------------------------------------------#