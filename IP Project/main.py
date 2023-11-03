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
            cursor.execute("CREATE TABLE IF NOT EXISTS EMPLOYEE (LOGINID VARCHAR(8), FIRST_NAME VARCHAR(30),LAST_NAME VARCHAR(30),DOB DATE,DEPT_NO VARCHAR(4),SALARY DECIMAL(10,2));")
            print(":--------- Select Tables ---------:")
            # dict_of_lst = 
except Exception as e:
    print(e)
