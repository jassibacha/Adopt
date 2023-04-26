from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "x87xs887sdf87sd8f9f9xjs"
debug = DebugToolbarExtension(app)

connect_db(app)
# with app.app_context():
#     db.create_all()
db.create_all()

@app.route('/')
def home():
    """Show all pets"""
    pets = Pet.query.all()
    """Show list of posts"""
    return render_template('home.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Show add pet form (GET) or handles form submission (POST)"""
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = True
        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)
        db.session.add(pet)
        db.session.commit()
        flash(f"{name} has been added!", "success")
        return redirect('/')
    else:
        return render_template('add-pet.html', form=form)

@app.route('/<int:pid>', methods=["GET", "POST"])
def view_edit_pet(pid):
    """Show the pets info and the editable fields (GET) or handle the form submission (POST)"""
    pet = Pet.query.get_or_404(pid)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash(f"{pet.name} has been updated!", "success")
        return redirect('/')
    else:
        return render_template('view-edit-pet.html', pet=pet, form=form)