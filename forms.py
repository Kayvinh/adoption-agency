from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField

class AddPetForm(FlaskForm):
    """Form for adding snacks."""

    name = StringField("Pet Name")
    species = StringField("Species")
    photo_url = StringField("Photo")
    age = StringField("Age")
    notes = TextAreaField("Additional Notes")