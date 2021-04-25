from flask import Flask, Blueprint
from flask import render_template, request, redirect
import repositories.beer_repository as beer_repository
import repositories.brewer_repository as brewer_repository
from models.beer import Beer
from models.brewer import Brewer

brewer_blueprint = Blueprint('brewer', __name__)

@brewer_blueprint.route('/brewers')
def brewers():
    brewers = brewer_repository.select_all()
    return render_template('brewers/index.html', all_brewers = brewers)