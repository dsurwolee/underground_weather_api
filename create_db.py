import sqlite3
from sql_util import *

def main():
	file_path = 'test.db'

	sql_create_table = """ CREATE TABLE weather (
							city text,
							state text,
							country text,
							zip integer,
							observation_time text,
							weather text,
							temp_f text,
							temp_c text,
							relative_humidity text,
							wind_mph text,
							precip_1hr_metric text
						); """

	# Create a database connection
	conn = db_connect(file_path)
	if conn is not None: 
		db_execute(conn, sql_create_table)
		conn.commit()
		conn.close()
	else:
		print("Error! cannot create a database connection.")

if __name__ == '__main__': 
	main()