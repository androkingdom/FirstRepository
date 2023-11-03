import pandas as pd
import mysql.connector as sqLtor

df = pd.read_csv("C:\\Users\\svm40\Desktop\\Class-XII Rishabh Madhwal\\IP Project\\user.csv" , names=["UserName","LoginId"])

# Function - 1 ==> This Function Create Login Id
def LoginId():
    import random
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    login_id = ''
    for i in range(2):
        login_id += random.choice(letters)
    for i in range(2):
        login_id += random.choice(letters)
    for j in range(2):
        numbers = random.randint(0, 10)
        login_id += str(numbers)
    for j in range(2):
        numbers = random.randint(0, 10)
        login_id += str(numbers)
    return login_id

# Function - 2 ==> This Function Create Database If Not Exist
def create_database(DatabaseName = "IPProjectDB"):
    try:
        myconnection = sqLtor.connect( host = 'localhost' , user = 'root', password = '1234')
        cursor = myconnection.cursor()
        cursor.execute(f'CREATE DATABASE IF NOT EXISTS {DatabaseName}')
        print ("Database created successfully")
        myconnection.close()
    except Exception as e:
        print(e)

# Function - 3 ==> This Function Delete Database
def drop_database(DatabaseName = "IPProjectDB"):
    try:
        myconnection = sqLtor.connect( host = 'localhost' , user = 'root', password = '1234')
        cursor = myconnection.cursor()
        cursor.execute(f'DROP DATABASE {DatabaseName}')
        print ("Database created deletd")
        myconnection.close()
    except Exception as e:
        print(e)

# Function - 4 ==> This Function Prevent Repetition Of UserName
def unique_(matchcase):
    global df
    for row in df.itertuples():
        lst_of_data = list(row)
        user_name = lst_of_data[1]
        if str(user_name).capitalize() == str(matchcase).capitalize():
            return False

# Function - 5 ==> This Function Login Using UserName And LoginID
def login(UserName,LoginID):
    global df
    for i in df.itertuples():
        if UserName == i[1] and LoginID == i[2]:
            return True
