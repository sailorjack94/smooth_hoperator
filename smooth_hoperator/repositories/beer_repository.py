from db.run_sql import run_sql
from models.brewer import Brewer


def save(beer):
    sql = "INSERT INTO beers (name, description, style, stock,  buy_price, sell_price, brewer_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *" 
    values = [beer.name, beer.description, beer.style, beer.stock, beer.buy_price, beer.sell_price, beer.brewer.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    beer.id = id
    return beer

def delete_all():
    sql = "DELETE FROM beers"
    run_sql(sql)