from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, StringField, URLField, PasswordField, BooleanField
from wtforms.validators import NumberRange, DataRequired, URL, Length, Optional


class EditPasswordGenerationForm(FlaskForm):
    description = StringField('Description', validators=[DataRequired(), Length(min=0, max=2000)])
    service_url = URLField('Service URL', validators=[DataRequired(), URL()])
    service_username = StringField('Service Username', validators=[Optional(), Length(min=5, max=20)])
    new_password = PasswordField('New Password', validators=[Optional(), Length(min=8)])
    generate_new = BooleanField('Generate New Password')
    length = IntegerField('Password Length', validators=[Optional(), NumberRange(min=8, max=64)])
    submit = SubmitField('Save Changes')
