from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,TextAreaField,SubmitField
from wtforms.validators import DataRequired

class EventForm(FlaskForm):
	event=StringField('Event',validators=[DataRequired()])
	hour=SelectField(choices=[('1','07:00')])
	discreption=TextAreaField('')
	type_e=SelectField(choices=[('1','training')])
	date=StringField('')
	save_e=SubmitField('Save Event')

class GoogleForm(FlaskForm):
	query_g=StringField('Search')
	submit_g=SubmitField('Google')