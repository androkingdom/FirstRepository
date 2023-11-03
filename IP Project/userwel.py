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

try:
    while True:
            cursor = connection.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS EMPLOYEE (LOGINID VARCHAR(8), FIRST_NAME VARCHAR(30),LAST_NAME VARCHAR(30),DOB DATE,DEPT_NO VARCHAR(4),SALARY DECIMAL(10,2));")

            print(":--------- Select Choice ---------:")
            dict_of_cho = {1 : "Insert" , 2 : "Retrieve",3 : "Delete" , 4 : "Exit"}
            for choice_number in dict_of_cho:
                 print(f"{choice_number} : {dict_of_cho[choice_number]}")
            print(":--------- ------------- ---------:")
            choice = int(input('Enter Choice Number : '))
            print(":--------- ------------- ---------:")
            
            match choice :
                 case 1 : 
                      pass
                 case 2 :
                      pass 
                 case 3 : 
                      pass
                 case 4 :
                      print("Program Exit") 
                      break
                 case _ :
                      print("Invalid Option")
                    
except Exception as e:
    print(e)
