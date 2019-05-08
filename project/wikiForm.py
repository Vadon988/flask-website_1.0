from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class WikiForm(FlaskForm):
	query=StringField(validators=[DataRequired()])
	submit=SubmitField('Wikipedia')