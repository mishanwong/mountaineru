from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField
import os

class SearchForm(FlaskForm):
    adventure = StringField('Adventure', validators=[DataRequired(message="Enter something")])
    difficulty = SelectField(u'Difficulty',
                choices=[('easy', 'Easy'), ('moderate', 'Moderate'), ('strenuous', 'Strenuous')])
    submit = SubmitField('Search')
