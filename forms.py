from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, AnyOf, URL

class AddPetForm(FlaskForm):
    """Form for adding pet"""

    name = StringField("Pet Name")

    species = SelectField(
        "Species",
        choices=[
            ('dog', 'Dog'),
            ('cat', 'Cat'),
            ('porcupine', 'Porcupine')
        ],
        validators=[InputRequired()]
    )

    photo_url = StringField(
        "Photo",
        validators=[Optional(), URL()]
    )


    age = SelectField(
        "Age",
        choices=[
            ('baby', 'Baby'),
            ('young', 'Young'),
            ('adult', 'Adult'),
            ('senior', 'Senior')
        ],
        validators=[
            InputRequired()
        ]
    )

    notes = TextAreaField("Additional Notes")


class EditPetForm(FlaskForm):
    """Form to edit pet details"""

    photo_url = StringField(
        "URL",
        validators=[Optional(), URL()]
    )

    notes = TextAreaField(
        "Notes"
    )

    available = BooleanField(
        "Available",
        validators=[InputRequired()]
    )