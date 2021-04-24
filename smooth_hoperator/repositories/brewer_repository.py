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

def select_all():
    brewers = []
    sql = "SELECT * FROM brewers ORDER BY id"
    results = run_sql(sql)

    for row in results:
        brewer = Brewer(row['name'], row['description'], row['id'])
        brewers.append(brewer)

    return brewers

def select(id):
    brewer = []
    sql = "SELECT * FROM brewers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)

    if result is not None:
        brewer = Brewer(result['name'], result['description'], result['id'])
    return brewer

def delete_all():
    sql = "DELETE FROM brewers"
    run_sql(sql)