from flask import render_template, url_for, flash,redirect, request, Blueprint, current_app
from VGGchallenge import  bcrypt, db
from VGGchallenge.models import User, Projects, Actions
from flask_login import login_user, current_user, logout_user, login_required 
from VGGchallenge.users.forms import registerForm, loginForm, updateAccountForm


users = Blueprint('users', __name__)



@users.route('/account', methods = ['GET', 'POST'])
@login_required
def account():
    form = updateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        db.session.commit()
        flash('your account has been updated', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
    return render_template('account.html', form = form)



@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated: 
        return redirect(url_for('projects.project'))
    form = loginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('projects.project'))
        else:
            flash('Invalid username or password', 'warning')
    return render_template('login.html', form = form)

@users.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated: 
        return redirect(url_for('projects.project'))
    form = registerForm()
    if form.validate_on_submit():
        hashPassword = bcrypt.generate_password_hash(form.password.data)
        user = User(username = form.username.data, password = hashPassword)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created !', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', form = form)

@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('users.login'))

