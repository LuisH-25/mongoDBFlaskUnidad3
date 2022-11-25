from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, DateField, IntegerField
from wtforms.validators import DataRequired


class BookForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    author = StringField("Authon", validators=[DataRequired()])
    pages = IntegerField("Pages number", validators=[DataRequired()])
    publish_date = DateField("Publish date", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    isbn = StringField("ISBN", validators=[DataRequired()])
    submit = SubmitField("Crear libro")

class RickandmortyForm(FlaskForm):
    id = IntegerField("Title", validators=[DataRequired()])
    name = StringField("Authon", validators=[DataRequired()])
    status = StringField("Pages number", validators=[DataRequired()])
    species = StringField("Publish date", validators=[DataRequired()])
    location = StringField("Description", validators=[DataRequired()])
    image = StringField("ISBN", validators=[DataRequired()])
    submit = SubmitField("Crear libro")
        