import pdb
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

@beer_blueprint.route('/beers/new')
def new_beer():
    beers = beer_repository.select_all()
    brewers = brewer_repository.select_all()
    return render_template("beers/new.html" ,all_brewers = brewers, all_beers = beers)

@beer_blueprint.route('/beers', methods = ["POST"])
def add_new_beer():
    name    = request.form['name']
    description = request.form['description']
    style = request.form['style']
    stock = request.form['stock']
    buy_price = request.form['buy_price']
    sell_price = request.form['sell_price']
    brewer  = brewer_repository.select(request.form['brewer_id'])
    beer = Beer(name, description, style, stock, buy_price, sell_price, brewer)
    beer_repository.save(beer)
    return redirect('/beers') 

@beer_blueprint.route('/stock')
def stock():
    beers = beer_repository.select_all()
    return render_template('beers/stock.html', all_beers = beers)

@beer_blueprint.route('/beers/<id>/edit')
def edit_beer(id):

    beer = beer_repository.select(id)
    brewers = brewer_repository.select_all()
    return render_template('beers/edit.html', beer=beer, all_brewers = brewers)

@beer_blueprint.route('/beers/<id>/delete', methods = ["POST"])
def delete_beer(id):
    beer_repository.delete(id)
    return redirect('/beers')