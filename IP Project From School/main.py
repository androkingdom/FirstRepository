import pandas as pd
import mysql.connector as sqLtor
# import Function as fn

def main_func():
    connection = sqLtor.connect(
        host="localhost",
        user="root",
        passwd="1234",
        database="project"
    )
    try:
        while True:
                dic_of_choice = {1 : "Insert", 2 : "Revert", 3 : "Delete"}
                print("---------------------")
                for choices in dic_of_choice:
                    print(f"{choices} - {dic_of_choice[choices]}")
                print("4 - close")
                choice = int(input("Enter choice : "))
                print("---------------------")
                print()
                print(":--------- Select Tables ---------:")




    except Exception as e:
        print(e)

main_func()