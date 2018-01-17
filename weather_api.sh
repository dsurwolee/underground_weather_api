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

	if [ -z $api ] || [ -z $config ] || [ -z $db ]; 
	then
		echo "Missing api, config, or db values required to run the script!"
		exit 1
	else
		echo Updating weather table...
		python data_pull/get_data.py $api $config $db
		echo Update success! 
	fi
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

	if [ -z $api ] || [ -z $config ] || [ -z $db ]; 
	then
		echo "Missing api, config, or db values required to run the script!"
		exit 1
	else
		while true; do
			python data_pull/get_data.py $api $config $db
			echo Weather table updated at date
			sleep $[60 * 60]
		done
	fi
}