import pandas as pd
import mysql.connector as sqLtor
import Function as fn

connection = sqLtor.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="project"
)
print(f"\nConnection Status : {connection.is_connected()}\n")

try:
    print(":--------- Select Tables ---------:")

    fn.show_databases()
    print(fn.database_dict)
    dict_of_database = fn.database_dict
    for db_no in dict_of_database:
        print(f"{db_no} : {dict_of_database[db_no]}")
    print()

except Exception as e :
    print(e)