from flask import Flask, Blueprint
from flask import render_template, request, redirect
import repositories.beer_repository as beer_repository
import repositories.brewer_repository as brewer_repository
from models.beer import Beer

beer_blueprint = Blueprint('beer', __name__)


# Page with all beers in the DB lists. In stock or otherwise.
@beer_blueprint.route('/beers')
def beers():
    beers = beer_repository.select_all()
    return render_template('beers/index.html', all_beers = beers)
