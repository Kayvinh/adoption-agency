import os
from flask import Flask, render_template, request, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import Pet, db, connect_db, DEFAULT_IMAGE_URL
from forms import AddPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///adopt')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "secret"

connect_db(app)

debug = DebugToolbarExtension(app)

@app.get('/')
def list_pets():
    """ List all pets available for adoption """

    pets = Pet.query.all()
    return render_template('list_pets.html', pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """ Display Pet add form, and handles the form """

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        flash(f"Added {name}!")
        return redirect("/add")
    
    else:
        return render_template("add_pet.html", form=form)

