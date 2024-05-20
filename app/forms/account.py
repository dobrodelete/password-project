from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, StringField, URLField, PasswordField, BooleanField
from wtforms.validators import NumberRange, DataRequired, URL, Length, Optional, ValidationError, EqualTo

from app.crud import bcrypt


class UpdatePasswordForm(FlaskForm):
    current_password = PasswordField('Current Password', validators=[DataRequired()])
    new_password = PasswordField('New Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm New Password', validators=[DataRequired(), EqualTo('new_password')])
    submit = SubmitField('Update Password')

    def validate_current_password(self, current_password):
        if not bcrypt.check_password_hash(current_user.password, current_password.data):
            raise ValidationError('Current password is incorrect.')
