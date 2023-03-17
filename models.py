from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = ""

def connect_db(app):
    """ Connect to database. """

    app.app_context().push()
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """ Models for adopt database """

    __tablename__ = "pets"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    name = db.Column(
        db.String(20),
        nullable=False
    )

    species = db.Column(
        db.String(20),
        nullable=False
    )

    photo_url = db.Column(
        db.Text,
        nullable=False,
        default = DEFAULT_IMAGE_URL
    )

    age = db.Column(
        db.String(10).in_(['baby', 'young', 'adult', 'senior']),
        nullable=False
    )

    notes = db.Column(
        db.Text,
        nullable=True
    )

    available = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )
