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

def unique(matchcase):
    for row in df.itertuples():
        lst_of_data = list(row)
        if str(lst_of_data[1]).capitalize() == str(matchcase).capitalize() or str(lst_of_data[1]) == "".capitalize():
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
def usernamecheaker(username):
    pass