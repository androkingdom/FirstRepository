import pandas as pd
import mysql.connector as sqLtor

df = pd.read_csv("C:\\Users\\andro\\OneDrive\\Desktop\\MYPROJECTS\\IP Project\\user.csv", names=["UserName", "LoginId"])

sample_conn = sqLtor.connect(
    host = "localhost",
    user = "root",
    passwd = "1234",
    database="project"
)

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


# Function - 2 ==> This Function Prevent Repetition Of User Name
def unique_(matchcase):
    global df
    for row in df.itertuples():
        lst_of_data = list(row)
        user_name = lst_of_data[1]
        if str(user_name).capitalize() == str(matchcase).capitalize():
            return False

# Function - 2 ==> This Function Login Using UserName And LoginID
def login(UserName,LoginID):
    for i in df.itertuples():
        if UserName == i[1] and LoginID == i[2]:
            return True
        
# Function - 3 ==> This Function Used To Make Table In Sql
def create_table(TableName):
    cursor = sample_conn.cursor()
    query = f"CREATE TABLE {TableName}"
    cursor.execute(query)

# Funtion - 4 ==> This Function Used To Find Whether user.csv Is Empty Or Not
def CsvIsEmpty():
    return True

# Funtion - 5 ==> This Function Used Specify The Length Of UserName
def AlphaInUserName(username):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    total = 0
    for letter in letters :
        if letter in username:
            if len(str(username)) >= 4 and len(str(username)) < 8:
                return True

# Function - 6 ==> This Function Create Database If Not Exist
def create_database(DatabaseName = "IPProjectDB"):
    try:
        myconnection = sqLtor.connect( host = 'localhost' , user = 'root', password = '1234')
        cursor = myconnection.cursor()
        cursor.execute(f'CREATE DATABASE IF NOT EXISTS {DatabaseName}')
        print ("Database created successfully")
        myconnection.close()
    except Exception as e:
        print(e)

# Function - 7 ==> This Function Delete Database
def drop_database(DatabaseName = "IPProjectDB"):
    try:
        myconnection = sqLtor.connect( host = 'localhost' , user = 'root', password = '1234')
        cursor = myconnection.cursor()
        cursor.execute(f'DROP DATABASE {DatabaseName}')
        print ("Database created deletd")
        myconnection.close()
    except Exception as e:
        print(e)