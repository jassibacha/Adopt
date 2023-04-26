from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Pets Model"""
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.Text, nullable=False, unique=True)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable=True, default='http://placekitten.com/400/400')
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    available = db.Column(db.Boolean, default=True)

    def __repr__(self):
        """Show info about pet."""
        p = self
        return f"<Pet id={p.id} name={p.name} species={p.species} age={p.age} available={p.available}>"
