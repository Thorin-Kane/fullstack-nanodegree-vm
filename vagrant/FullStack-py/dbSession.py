import sqlite3
from flask import g

DATABASE = '/vagrant/Fullstack-py/restaurantmenu.db'

def get_db():
	db = getattr(g,'_database', None)
	if db is None:
		db = g._database = connect_to_database()
	return db

def query_db(query,args = (), one=False):
	db = get_db().execute(query,args)
	val = db.fetchall()
	db.close()
	return(val[0] if val else None) if one else val

@app.teardown_appcontext
def close_connnection(exception):
	db=getattr(g,'_database',None)
	if db is not None:
		db.close()