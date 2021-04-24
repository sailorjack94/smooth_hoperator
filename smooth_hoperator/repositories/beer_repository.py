from db.run_sql import run_sql
from models.brewer import Brewer
from models.beer import Beer
import respositories.brewer_repository as brewer_repository


def save(beer):
    sql = "INSERT INTO beers (name, description, style, stock,  buy_price, sell_price, brewer_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *" 
    values = [beer.name, beer.description, beer.style, beer.stock, beer.buy_price, beer.sell_price, beer.brewer.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    beer.id = id
    return beer
    
def select_all():
    beers = []
    sql = 'SELECT * FROM beers ORDER BY id'
    results = run_sql(sql)

    for row in results:
        brewer = brewer.respository.select(row['brewer.id'])
        beer = Beer(row['name'], row['description'], row['style'], row['stock'], row['buy_price'], row['sell_price'], brewer, row['id'])
        beers.append(beer)
    return beers


def delete_all():
    sql = "DELETE FROM beers"
    run_sql(sql)