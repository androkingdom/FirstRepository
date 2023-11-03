import pandas as pd
import mysql.connector as sqLtor
from sqlalchemy import create_engine
import Function as fn
import login as log

try:
    while True:
            dbengine1 = create_engine("mysql+pymysql://root:1234@localhost/project")
            connection = dbengine1.connect()
            conn = sqLtor.connect(host="localhost",user="root",passwd="1234",database="project")
            cursor = conn.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS EMPLOYEE (LOGINID VARCHAR(8), FIRST_NAME VARCHAR(30),LAST_NAME VARCHAR(30),DOB DATE,DEPT_NO VARCHAR(4),SALARY DECIMAL(10,2));")

            print(":--------- Select Choice ---------:")
            dict_of_cho = {1 : "Insert" , 2 : "Retrieve",3 : "Delete" , 4 : "Exit"}
            for choice_number in dict_of_cho:
                 print(f"{choice_number} : {dict_of_cho[choice_number]}")
            print(":--------- ------------- ---------:")
            choice = int(input('Enter Choice Number : '))
            print(":--------- ------------- ---------:")
            print()
            
            match choice :
                 case 1 : 
                      pass
                 case 2 :
                      df = pd.read_sql("Select * from Employee",connection)
                      if df.empty:
                           print("No Data Found!!")
                           print()
                      else:
                           print(df)  
                 case 3 : 
                      pass
                 case 4 :
                      print("Program Exit") 
                      break
                 case _ :
                      print("Invalid Option")
                    
except Exception as e:
    print(e)
