from db.run_sql import run_sql
from models.brewer import Brewer
from models.beer import Beer 

def save(brewer):
    sql = "INSERT INTO brewers (name, description) VALUES (%s, %s) RETURNING *"
    values = [brewer.name, brewer.description]
    results = run_sql(sql, values)
    id = results[0]['id']
    brewer.id = id 
    return brewer

def delete_all():
    sql = "DELETE FROM brewers"
    run_sql(sql)