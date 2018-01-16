import sqlite3
import requests 
import json
import sys

from sql_util import *

def fetch_data(url):
	""" Executes a get request based on 
		url
	:param url: api url pattern 
	:return: response
	"""
	try: 
		r = requests.get(url) 
		return r.json()
	except requests.exceptions.RequestException as e:
		print(e)

	return None

def create_url_pattern(api, state, city):
	""" Generates an appropriate pattern
		based on api, state and city defined
	:param api: user api key
	:param state: state to search
	:param city: city to search
	:return: api pattern 
	"""
	return 'http://api.wunderground.com/api/{api_key}/conditions/' \
		   'q/{state}/{city}.json'.format(api_key=api, state=state, city=city)


def query_dict(d, query):
	""" Queries a nested json based on query 
		statement
	:parmm d: nested json
	:param query: query statement
	:return: value
	"""
	keys = query.split('/')
	for k in keys:
	    d = d[k]
	return d

def main():

	sysargs = sys.argv[1:]
	if len(sysargs) == 3:
		api_key = sysargs[0]
		config = sysargs[1]
		db_file = sysargs[2]
	else: 
		raise Exception('Parameter missing!')

	# Get variables from json file
	outer_key = 'current_observation/'
	display_key = outer_key + 'display_location/'
	with open(config, 'r') as f:
		file = json.load(f)
		loclist = [(kv['city'], kv['state']) for kv in query_dict(file, 'locations')]
		outer = [display_key + s for s in query_dict(file, 'vars/display')]
		local = [outer_key + s for s in query_dict(file, 'vars/outer')]
		queries = outer + local

	# Request data from API and store result into list
	vlist = []
	for city, state in loclist:
		url = create_url_pattern(api_key, state, city)
		resp = fetch_data(url)
		v = tuple(query_dict(resp, q) for q in queries)
		vlist.append(v)

	# Execute sql statements to database
	bindings = '?, ' * len(queries)
	sql_update_table = """INSERT INTO weather VALUES ({0})""".format(bindings[:-2])
	conn = db_connect(db_file)
	db_execute_many(conn, sql_update_table, vlist)
	conn.commit()
	conn.close()

if __name__ == '__main__':
	main() 
