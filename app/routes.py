import os
import secrets
import string

from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_bcrypt import Bcrypt
from flask_login import logout_user, login_required, current_user, login_user

from app.crud import get_user_by_email
from app.forms import RegistrationForm, LoginForm
from app.forms.password import PasswordGenerationForm
from app.models import User, db, Password

main = Blueprint('main', __name__, static_folder="app/templates/static")
bcrypt = Bcrypt()


@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created!', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', title='Register', form=form)


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = get_user_by_email(email=form.email.data)
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Your success login!', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Username or password invalid!', 'error')
            return render_template('login.html', title='Home', form=form)
    return render_template('login.html', title='Login', form=form)


@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@main.route('/account')
@login_required
def account():
    return render_template('account.html', title='Account')


@main.route('/', methods=['GET', 'POST'])
def home():
    form = PasswordGenerationForm()
    generated_password = None
    if form.validate_on_submit():
        length = form.length.data
        characters = string.ascii_letters + string.digits + string.punctuation
        generated_password = ''.join(secrets.choice(characters) for _ in range(length))
        flash('Password generated successfully!', 'success')

    if request.method == 'POST' and 'save_password' in request.form:
        username = request.form['username']
        service_url = request.form['service_url']
        password = request.form['password']
        print(request.form)
        new_password = Password(
            description="Generated Password",
            service_url=service_url,
            service_username=username,
            password=password,
            user_id=current_user.id
        )
        new_password.encrypt_password(password, os.environ.get('FERNET_KEY').encode())
        db.session.add(new_password)
        db.session.commit()
        flash('Password saved successfully!', 'success')
        return redirect(url_for('main.home'))

    return render_template('home.html', form=form, generated_password=generated_password)
