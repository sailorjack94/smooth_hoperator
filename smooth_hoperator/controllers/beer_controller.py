import pdb
from flask import Flask, Blueprint
from flask import render_template, request, redirect
import repositories.beer_repository as beer_repository
import repositories.brewer_repository as brewer_repository
from models.beer import Beer

beer_blueprint = Blueprint('beer', __name__)


# Page with all beers in the DB lists. In stock or otherwise. Base for Beer Management Page.
@beer_blueprint.route('/beers', methods = ['GET'])
def beers():
    beers = beer_repository.select_all()
    brewers = brewer_repository.select_all()
    return render_template('beers/stock.html', all_beers = beers, all_brewers=brewers)

# Filter beers by brewer.
@beer_blueprint.route('/beers', methods = ['POST'])
def test():
    beers = beer_repository.select_all()
    brewers = brewer_repository.select_all()
    brewer  = brewer_repository.select(request.form['brewer_id'])
    return render_template('beers/test.html', all_beers = beers, all_brewers=brewers, brewer=brewer)

@beer_blueprint.route('/beers/name')
def beers_by_name():
    return redirect('/beers')


@beer_blueprint.route('/beers/stock')
def beers_by_stock():
    beers = beer_repository.select_all_by_stock()
    return render_template('beers/stock.html', all_beers = beers)

@beer_blueprint.route('/beers/cost')
def beers_by_cost():
    beers = beer_repository.select_all_by_cost()
    return render_template('beers/stock.html', all_beers = beers)

@beer_blueprint.route('/beers/brewer')
def beers_by_brewer():
    beers = beer_repository.select_all_order_by_brewer()
    return render_template('beers/stock.html', all_beers = beers)

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

# HERE
@beer_blueprint.route('/beers/new', methods = ["POST"])
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

# @beer_blueprint.route('/stock', methods=['GET'])
# def sort_by_query_string():
#     query = request.query_string
#     if "sortn" in query:
#         return query


@beer_blueprint.route('/stock')
def stock():
    beers = beer_repository.select_all()
    return render_template('beers/index.html', all_beers = beers)

@beer_blueprint.route('/beers/<id>/edit', methods=['GET'])
def edit_beer(id):
    beer = beer_repository.select(id)
    brewers = brewer_repository.select_all()
    return render_template('beers/edit.html', beer=beer, all_brewers = brewers)

@beer_blueprint.route("/beers/<id>", methods=['POST'])
def update_beer(id):
    name    = request.form['name']
    description = request.form['description']
    style   = request.form['style']
    stock = int(request.form['stock'])
    buy_price = float(request.form['buy_price'])
    sell_price = float(request.form['sell_price'])
    brewer_id = int(request.form['brewer'])
    brewer  = brewer_repository.select(brewer_id)
    beer = Beer(name, description, style, stock, buy_price, sell_price, brewer, int(id))
    beer_repository.update(beer)
    return redirect('/stock')


@beer_blueprint.route('/beers/<id>/delete', methods = ["POST"])
def delete_beer(id):
    beer_repository.delete(id)
    return redirect('/beers')
