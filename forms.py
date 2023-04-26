from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Email, Length, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    """Add A Pet!"""
    name = StringField("Name", validators=[InputRequired()])
    #species = StringField("Species", validators=[InputRequired()])
    species = SelectField("Species", choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=1, max=30, message="Age must be between 1-30")])
    notes = TextAreaField("Notes", validators=[Optional(), Length(min=10)])

class EditPetForm(FlaskForm):
    """Edit some of the pet values"""
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = TextAreaField("Notes", validators=[Optional(), Length(min=10)])
    available = BooleanField("Available")