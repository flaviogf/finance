from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import login_user

from app.models import User
from app.user.forms import LoginForm

user = Blueprint('user', __name__)


@user.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and user.authenticate(form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('core.home'))

        flash('Check your email or password.')

    return render_template('login.html', form=form)


@user.route('/register')
def register():
    return render_template('register.html')
