from flask import (Blueprint, current_app, flash, redirect, render_template,
                   url_for, request)
from flask_login import current_user, login_required, login_user, logout_user

from app import db
from app.models import User
from app.user.forms import LoginForm, RegisterForm

user = Blueprint('user', __name__)


@user.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and user.authenticate(form.password.data):
            login_user(user, remember=form.remember.data)

            next_url = request.args.get('next')

            return redirect(next_url or url_for('core.home'))

        flash('Check your email or password.')

    return render_template('login.html', title='Login', form=form)


@user.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        password_hash = User.generate_password_hash(form.password.data)

        user = User(name=form.name.data,
                    email=form.email.data,
                    password=password_hash)

        db.session.add(user)

        db.session.commit()

        user.send_welcome_message()

        return redirect(url_for('user.login'))

    return render_template('register.html', title='Register', form=form)


@user.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('user.login'))
