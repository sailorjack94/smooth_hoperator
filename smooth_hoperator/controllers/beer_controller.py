from flask import Flask, Blueprint
from flask import render_template, request, redirect
import repositories.beer_repository as beer_repository
import repositories.brewer_repository as brewer_repository
from models.beer import Beer

beer_blueprint = Blueprint('beer', __name__)


# Page with all beers in the DB lists. In stock or otherwise. Base for Beer Management Page.
@beer_blueprint.route('/beers')
def beers():
    beers = beer_repository.select_all()
    return render_template('beers/index.html', all_beers = beers)

# Returns all details for a selected beer. Use for edit beer page.
@beer_blueprint.route('/beers/<id>', methods = ['GET'])
def show_beer(id):
    beer = beer_repository.select(id)
    return render_template('beers/show.html', beer = beer)
