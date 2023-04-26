"""Seed file to make sample data for pets db."""

from models import Pet, db
from app import app

# Create all tables
# with app.app_context():
#     db.drop_all()
#     db.create_all()
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

pets = [
    {"name": "Icecream", "species": "cat", "photo_url": "https://wildcard.codestuff.io/cat/250/250", "age": 6, "notes": "A fluffy cat.", "available": True},
    {"name": "Buddy", "species": "dog", "photo_url": "https://wildcard.codestuff.io/dog/250/250", "age": 3, "notes": "A friendly dog.", "available": True},
    {"name": "Fluffy", "species": "cat", "photo_url": "https://wildcard.codestuff.io/cat/300/300", "age": 2, "notes": "A playful cat.", "available": False},
    {"name": "Fido", "species": "dog", "photo_url": "https://wildcard.codestuff.io/dog/300/300", "age": 5, "notes": "A loyal dog.", "available": True},
    {"name": "Quill", "species": "porcupine", "photo_url": "https://wildcard.codestuff.io/tiger/300/300", "age": 1, "notes": "A prickly porcupine.", "available": True},
    {"name": "Simba", "species": "cat", "photo_url": "https://wildcard.codestuff.io/cat/400/400", "age": 4, "notes": "A regal cat.", "available": True},
    {"name": "Snoopy", "species": "dog", "photo_url": "https://wildcard.codestuff.io/dog/400/400", "age": 7, "notes": "A fun-loving dog.", "available": False},
    {"name": "Hedgie", "species": "porcupine", "photo_url": "https://wildcard.codestuff.io/tiger/350/350", "age": 2, "notes": "A cute porcupine.", "available": True},
    {"name": "Loki", "species": "cat", "photo_url": "https://wildcard.codestuff.io/dog/450/450", "age": 1, "notes": "A mischievous cat.", "available": True},
    {"name": "Rufus", "species": "dog", "photo_url": "https://wildcard.codestuff.io/dog/350/350", "age": 9, "notes": "A wise old dog.", "available": True},
]


# Add new objects to session, so they'll persist
for pet in pets:
    p = Pet(
        name=pet["name"],
        species=pet["species"],
        photo_url=pet["photo_url"],
        age=pet["age"],
        notes=pet["notes"],
        available=pet["available"]
    )
    db.session.add(p)

# Commit--otherwise, this never gets saved!
db.session.commit()