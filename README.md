# Underground Weather API 

## List of files
| File                  | Purpose       |
| --------------------- | ------------- |
| `config.json`         | Specifies variables and locations to request from Underground API. |
| `create_db.py`        | The file creates a SQLite3 database under the name 'test.db' in the current path. |
| `sql_util.py`         | File containing useful SQLite3 functions. |
| `weather_api.py`      | Main Python file for pulling and inserting data. |
| `weather_api.sh`      | Shell script functions for creating, pulling and exporting data. |


### Instruction

```
1) In command line, source weather_api.sh to export shell functions
2) Run 'create_db' to create a SQLite3 database. This will create a db called "test.db" in the main path,
3) Run 'get_data' to pull data from Underground Weather and update the db. Input your api key, path to the test.db and path to the config file in the config folder
```

To auto-update table at a 60 minute increment, run the following shell function:
```
stream_data
```

To output the table into csv, run:
```
export_data
```
