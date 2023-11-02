import pandas as pd
import mysql.connector as sqLtor
import Function as fn
import login as log

connection = sqLtor.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="project"
)

# if __name__ == "__main__":
try:
    while True:
            cursor = connection.cursor()
            print(":--------- Select Tables ---------:")
            print(log.User_Name)

            



except Exception as e:
    print(e)
