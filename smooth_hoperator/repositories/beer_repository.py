from db.run_sql import run_sql
from models.brewer import Brewer
from models.beer import Beer
import repositories.brewer_repository as brewer_repository


def save(beer):
    sql = "INSERT INTO beers (name, description, style, stock,  buy_price, sell_price, brewer_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *" 
    values = [beer.name, beer.description, beer.style, beer.stock, beer.buy_price, beer.sell_price, beer.brewer.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    beer.id = id
    return beer

    
def select_all():
    beers = []
    sql = "SELECT * FROM beers ORDER BY name ASC"
    results = run_sql(sql)

    for row in results:
        brewer = brewer_repository.select(row['brewer_id'])
        beer = Beer(row['name'], row['description'], row['style'], row['stock'], row['buy_price'], row['sell_price'], brewer, row['id'])
        beers.append(beer)
    return beers

def select_all_by_stock():
    beers = []
    sql = "SELECT * FROM beers ORDER BY stock DESC"
    results = run_sql(sql)
    for row in results:
        brewer = brewer_repository.select(row['brewer_id'])
        beer = Beer(row['name'], row['description'], row['style'], row['stock'], row['buy_price'], row['sell_price'], brewer, row['id'])
        beers.append(beer)
    return beers

def select_all_by_cost():
    beers = []
    sql = "SELECT * FROM beers ORDER BY sell_price ASC"
    results = run_sql(sql)
    for row in results:
        brewer = brewer_repository.select(row['brewer_id'])
        beer = Beer(row['name'], row['description'], row['style'], row['stock'], row['buy_price'], row['sell_price'], brewer, row['id'])
        beers.append(beer)
    return beers

def select_all_order_by_brewer():
    beers = []
    sql = "SELECT * FROM beers ORDER BY brewer_id ASC"
    results = run_sql(sql)
    for row in results:
        brewer = brewer_repository.select(row['brewer_id'])
        beer = Beer(row['name'], row['description'], row['style'], row['stock'], row['buy_price'], row['sell_price'], brewer, row['id'])
        beers.append(beer)
    return beers

def select(id):
    beer = None
    sql = 'SELECT * FROM beers WHERE id = %s'
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        brewer = brewer_repository.select(result['brewer_id'])
        beer = Beer(result['name'], result['description'], result['style'], result['stock'], result['buy_price'], result['sell_price'], brewer, result['id'])
    return beer

def select_by_brewer(brewer_id):
    beers = []
    sql = "SELECT * FROM beers WHERE brewer_id = %s"
    values = [brewer_id]
    results = run_sql(sql, values)

    for row in results:
        brewer = brewer_repository.select(row['brewer_id'])
        beer = Beer(row['name'], row['description'], row['style'], row['stock'], row['buy_price'], row['sell_price'], brewer, row['id'] )
        beers.append(beer)
    return beers




def delete_all():
    sql = "DELETE FROM beers"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM beers WHERE id = %s"
    values = [id]
    run_sql(sql,values)



def select_all_by_brewer(brewer_id):
    beers = []
    sql = "SELECT * FROM beers WHERE brewer_id = %s"
    values = [brewer_id]
    results = run_sql(sql, values)

    for row in results:
        brewer = brewer_repository.select(row['brewer_id'])
        beer = Beer(row['name'], row['description'], row['style'], row['stock'], row['buy_price'], row['sell_price'], brewer, row['id'])
        beers.append(beer)
    return beers




def update(beer):
    sql = "UPDATE beers SET (name, description, style, stock, buy_price, sell_price, brewer_id) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [beer.name, beer.description, beer.style, beer.stock, beer.buy_price,beer.sell_price, beer.brewer.id, beer.id]
    run_sql(sql, values)

def total_value():
    value = 0
    sql= "SELECT SUM(buy_price * stock) FROM beers"
    value = run_sql(sql)
