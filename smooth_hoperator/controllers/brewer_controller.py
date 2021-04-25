from flask import Flask, Blueprint
from flask import render_template, request, redirect
import repositories.beer_repository as beer_repository
import repositories.brewer_repository as brewer_repository
from models.beer import Beer
from models.brewer import Brewer

brewer_blueprint = Blueprint('brewer', __name__)

# Returns all brewers on one page. Base for Brewer Managment Page.
@brewer_blueprint.route('/brewers')
def brewers():
    brewers = brewer_repository.select_all()
    return render_template('brewers/index.html', all_brewers = brewers)

# Returns all detail on selected brewers. User for edit brewer page.
@brewer_blueprint.route('/brewers/<id>', methods = ["GET"])
def show_brewer(id):
    brewer = brewer_repository.select(id)
    return render_template('brewers/show.html', brewer = brewer)

# Add Brewer Page
@brewer_blueprint.route('/brewers/new')
def new_brewer():
    return render_template("brewers/new.html")

@brewer_blueprint.route('/brewers', methods = ["POST"])
def add_new_brewer():
    name    = request.form['name']
    description = request.form['description']
    brewer = Brewer(name, description)
    brewer_repository.save(brewer)
    return redirect('/brewers') 