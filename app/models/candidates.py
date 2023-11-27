"""Candidate Database Model

This module defines the Candidate class, representing candidates 
in the system.
It utilizes SQLAlchemy to interact with the database.

Classes:
    Candidate: Represents a candidate in the system.

Note:
    This module assumes the existence of a Flask application instance
    and the 'db' object defined within the 'app.models' module.

Example:
    # Create a new candidate
    new_candidate = Candidate(
        firstname='John',
        lastname='Doe',
        email='john@example.com',
        age=30
    )
    db.session.add(new_candidate)
    db.session.commit()
"""

from sqlalchemy.sql import func
from app import db

print("lolllll")


# pylint: disable=too-few-public-methods
class Candidate(db.Model):
    """Candidate Model

    Represents a candidate in the system.
    """

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100))
    email = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
