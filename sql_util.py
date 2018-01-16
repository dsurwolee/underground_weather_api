import sqlite3

def db_connect(file):
	""" connect to the database specified
		by the file
	:param file: db file
	:return: connection object or None
	"""
	try: 
		conn = sqlite3.connect(file)
		return conn
	except sqlite3.Error as e:
		print(e)

	return None

def db_execute(conn, sql_statement):
	""" execute from the sql_statement 
	:param conn: connection object
	:param sql_statement: sql statement to execute  
	:return: None 
	"""
	try:
		c = conn.cursor()
		conn.execute(sql_statement)
	except sqlite3.Error as e:
		print(e)

	return None

def db_execute_many(conn, sql_statement, values):
	""" execute multiple sql statements
	:param conn: connection object
	:param sql_statement: sql statement to execute  
	:return: None 
	"""
	try:
		c = conn.cursor()
		conn.executemany(sql_statement, values)
	except sqlite3.Error as e:
		print(e)

	return None
