from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField
import os

class SearchForm(FlaskForm):
    adventure = StringField('Adventure', validators=[DataRequired()])
    startdate = DateField('Start Date', format='%Y-%m-%d')
    enddate = DateField('End Date', format='%Y-%m-%d')
    submit = SubmitField('Search')