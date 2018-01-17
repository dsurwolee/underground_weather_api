#!/bin/bash

# Creates a database
create_db()
{
	echo Creating table...
	python data_pull/create_db.py 
	echo Table created!
}

# Fetches data from Underground Weather
get_data() 
{
	read -p 'Please enter your Weather Underground API key: ' api
	read -p 'Please enter the path to your config file: ' config
	read -p 'Please enter your database path: ' db

	echo Updating weather table...
	python data_pull/get_data.py $api $config $db
	echo Update success! 
}


# Exports data to csv
export_data() 
{
	echo Exporting data...
	sqlite3 -header -csv test.db "select * from weather;" > data.csv
	echo Data exported!
}

# Streams data at 60 minute increment
stream_data()
{
	read -p 'Please enter your Weather Underground API key: ' api
	read -p 'Please enter the path to your config file: ' config
	read -p 'Please enter your database path: ' db

	while true; do
		python data_pull/get_data.py $api $config $db
		echo Weather table updated at date
		sleep $[60 * 60]
	done
}