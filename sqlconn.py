import pandas as pd
import mysql.connector as sqLtor
from sqlalchemy import create_engine

def insert_query():
    global strnglst
    global lst_of_record
    global use_str
    tup_of_records = tuple(lst_of_record)
    mycursor = connection2.cursor()
    query = f"insert into {table_name} values {use_str}"
    mycursor.execute(query, tup_of_records)
    connection2.commit()
    print(f"-----------\n{mycursor.rowcount} record inserted.\n-----------")
    lst_of_record.clear()
    strnglst.clear()
 
def delete_query(primfield , primkey , tbname):
    mycursor = connection2.cursor()
    query = f"delete from {tbname} where {primfield} = {primkey}"
    mycursor.execute(query)
    connection2.commit()
    print(f"-----------\n{mycursor.rowcount } record deleted.\n-----------")
 
#  def drop_field():

try:
    dbengine = create_engine("mysql+pymysql://root:1234@localhost/classxiib")
 
    connection1 = dbengine.connect()
 
    connection2 = sqLtor.connect(
        host = 'localhost' ,
        user = 'root' , 
        passwd = '1234' , 
        database = "classxiib"
    )

    mycursor = connection2.cursor()
    mycursor.execute("show tables")
    for table_name in mycursor:
        print(table_name)


    table_name = input("-----------------\nEnter table name : ")
    print("-----------------")
    lst_of_record = []
    strnglst = []
 
    df1 = pd.read_sql(f"select * from {table_name} ;" , connection1)
    column_of_df1 = df1.columns
    lst_of_column = list(column_of_df1)
    print(df1)

    while True:
        
        dic_of_choice = {1 : "Insert", 2 : "Revert", 3 : "Delete"}
        print("---------------------")
        for choices in dic_of_choice:
            print(f"{choices} - {dic_of_choice[choices]}")
        print("4 - close")
        choice = int(input("Enter choice : "))
        print("---------------------")
        match choice:
            case 1 :
                for field in lst_of_column:
                    records = input(f"Enter {field} : ")
                    lst_of_record.append(records)
                    strnglst.append("%s")
                tup = tuple(strnglst)
                strg = ",".join(tup)
                use_str = f"({strg})"
                insert_query()
            case 2 :
                pass
            case 3 : 
                tbname = table_name
                primfield = input("Enter unique field name : ")
                primkey = input("Enter field id : ")
                delete_query(primfield , primkey , tbname)
            case 4 :
                print("Loop Exit")
                break
            case _ :
                print("Wrong Input")
 
        dbengine1 = create_engine("mysql+pymysql://root:1234@localhost/classxiib")
 
        connection2a= dbengine.connect()
        df2 = pd.read_sql(f"select * from {table_name}" , connection2a)
        print(df2)
        
except Exception as e :
    print(e)
    print("Program Exit")
 
# connection1.close()
# connection2.close()
