from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, StringField, URLField
from wtforms.validators import NumberRange, DataRequired, URL, Length


class PasswordGenerationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    service_url = URLField('Service URL', validators=[DataRequired(), URL()])
    length = IntegerField('Password Length', validators=[DataRequired(), NumberRange(min=8, max=64)])
    submit = SubmitField("Generate Password")
