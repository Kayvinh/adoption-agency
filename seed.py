from models import Pet, db
from app import app

db.drop_all()
db.create_all()

# Add Pets
pet1 = Pet(
    name="Woofly",
    species="Dog",
    photo_url="https://hips.hearstapps.com/hmg-prod/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg?crop=0.752xw:1.00xh;0.175xw,0&resize=1000:*",
    age = 'baby',
    notes="hates people"
)

pet2 = Pet(
    name="Snargle",
    species="Cat",
    photo_url="https://hips.hearstapps.com/hmg-prod/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg?crop=0.752xw:1.00xh;0.175xw,0&resize=1000:*",
    age = 'young',
    notes="loves people"
)

pet3 = Pet(
    name="Kevin",
    species="Donkey",
    age = 'baby'
)

# Add new objects to session
db.session.add(pet1)
db.session.add(pet2)
db.session.add(pet3)

# commit
db.session.commit()