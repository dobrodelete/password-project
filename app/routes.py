import os
import secrets
import string

from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_bcrypt import Bcrypt
from flask_login import logout_user, login_required, current_user, login_user

from app.crud import get_user_by_email
from app.forms import RegistrationForm, LoginForm, UpdatePasswordForm
from app.forms.edit_password import EditPasswordGenerationForm
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


@main.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdatePasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.new_password.data).decode('utf-8')
        current_user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated!', 'success')
        return redirect(url_for('main.account'))
    return render_template('account.html', title='Account', form=form)


@main.route('/update_password', methods=['GET', 'POST'])
@login_required
def update_password():
    ...


@main.route('/', methods=['GET', 'POST'])
@login_required
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


@main.route('/passwords')
@login_required
def passwords():
    user_passwords = Password.query.filter_by(user_id=current_user.id).all()
    key = os.environ.get('FERNET_KEY').encode()
    for password in user_passwords:
        password.password = password.decrypt_password(key)
    return render_template('passwords.html', passwords=user_passwords)


@main.route('/passwords/edit/<int:password_id>', methods=['GET', 'POST'])
@login_required
def edit_password(password_id):
    password = Password.query.get_or_404(password_id)
    if password.owner != current_user:
        flash('You do not have permission to edit this password.', 'danger')
        return redirect(url_for('main.passwords'))

    form = EditPasswordGenerationForm(
        description=password.description,
        service_url=password.service_url,
        service_username=password.service_username,
        length=12
    )

    if form.validate_on_submit():
        password.description = form.description.data
        password.service_url = form.service_url.data
        password.service_username = form.service_username.data

        if form.new_password.data:
            password.encrypt_password(form.new_password.data, os.environ.get('FERNET_KEY').encode())
        elif form.generate_new.data and form.length.data:
            length = form.length.data
            characters = string.ascii_letters + string.digits + string.punctuation
            generated_password = ''.join(secrets.choice(characters) for _ in range(length))
            password.encrypt_password(generated_password, os.environ.get('FERNET_KEY').encode())
            flash(f'New password generated: {generated_password}', 'info')

        db.session.commit()
        flash('Password updated successfully!', 'success')
        return redirect(url_for('main.passwords'))

    return render_template('edit_password.html', form=form, password=password)


@main.route('/passwords/delete/<int:password_id>')
@login_required
def delete_password(password_id):
    password = Password.query.get_or_404(password_id)
    if password.owner != current_user:
        flash('You do not have permission to delete this password.', 'danger')
        return redirect(url_for('main.passwords'))

    db.session.delete(password)
    db.session.commit()
    flash('Password deleted successfully!', 'success')
    return redirect(url_for('main.passwords'))


@main.route('/passwords/export/<int:password_id>')
@login_required
def export_password(password_id):
    password = Password.query.get_or_404(password_id)
    if password.owner != current_user:
        flash('You do not have permission to export this password.', 'danger')
        return redirect(url_for('main.passwords'))

    decrypted_password = password.decrypt_password(os.environ.get('FERNET_KEY').encode())
    flash(f'Password: {decrypted_password}', 'info')
    return redirect(url_for('main.passwords'))
