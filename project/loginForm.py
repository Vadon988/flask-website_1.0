from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired,Email

class LoginForm(FlaskForm):
	username=StringField(validators=[DataRequired()])
	email=StringField(validators=[DataRequired()])
	password=StringField(validators=[DataRequired()])
	login=SubmitField()

class LogoutForm(FlaskForm):
	username=StringField()
	logout=SubmitField('Logout')