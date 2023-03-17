import os
from flask import Flask, render_template, request, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import Pet, db, connect_db, DEFAULT_IMAGE_URL
from forms import AddPetForm, EditPetForm

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

        new_pet = Pet(
            name=name,
            species=species,
            photo_url=photo_url,
            age=age,
            notes=notes
        )

        db.session.add(new_pet)
        db.session.commit()

        flash(f"Added {name}!")
        return redirect("/")

    else:
        print("HIT RENDER TEMPLATE")
        return render_template("add_pet.html", form=form)

@app.route("/<int:pid>", methods=["GET", "POST"])
def pet_detail(pid):
    """Display pet info and form to edit pet info"""

    pet = Pet.query.get_or_404(pid)

    form = EditPetForm()

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        return redirect(f"/{pid}")

    else:
        return render_template("pet_detail.html", form=form, pet=pet)



