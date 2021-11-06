from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField


class FSearch(FlaskForm):
    search_field = TextField(label='Search')
    submit_field = SubmitField(label='جست و جو')
