from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    query = StringField('Search', validators=[DataRequired()])
    submit = SubmitField('Search')
# Path: app/routes.py
# Function name: search
# Description: This function is used to handle the search functionality. It retrieves the search query from the request arguments, filters the videos based on the query, and renders the search.html template with the filtered videos.