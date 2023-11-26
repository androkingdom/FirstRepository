import random
import style
import pandas as pd
import mysql.connector as sqLtor
import datetime


def result(usersel , compu):

    dic = {1:{2:"loss",3:"won",1:"draw"},
    2:{3:"loss",1:"won",2:"draw"},
    3:{1:"loss",2:"won",3:"draw"}}

    meaning = {1:"Rock",2:"Paper",3:"Scissor"}

    if usersel not in dic:
        print("Your : Enter Invaild Input")

    elif compu not in dic:
        print("Comp. : Enter Invaild Input")
        print(compu)

    else:
        print()
        user = dic[usersel]
        result = user[compu]
        print(f"Your : {meaning[usersel]}")
        print(f"Comp. : {meaning[compu]}")
        style.style(f"Result : {result}")

# 1=> rock --> 2=> paper
# 2=> paper --> 3=> scissor
# 3=> scissor --> 1=> rock


def HardLevel(usersel):
    CompuResult = 0 
    user = usersel
    Score = 0
    OutputDict = {}
    HardGameDict = {1:2,2:3,3:1}
    EasyGameDict = {1:3,2:1,3:2}
    HardChance = random.randint(1,100)
    if HardChance <= 90 and HardChance >= 1:
        CompuResult = HardGameDict[user]
    elif HardChance < 95  and HardChance > 90 :
        CompuResult = user
    else :
        CompuResult = EasyGameDict[user]
        Score += 1
    OutputDict["CompuResult"] = CompuResult
    OutputDict["Score"] = Score
    return OutputDict

def EasyLevel(usersel):
    CompuResult = 0 
    user = usersel
    Score = 0
    OutputDict = {}
    EasyChance = random.randint(1,100)
    HardGameDict = {1:2,2:3,3:1}
    EasyGameDict = {1:3,2:1,3:2}
    if EasyChance <= 90 and EasyChance >= 1:
        CompuResult = EasyGameDict[user]
        Score += 1
    elif EasyChance < 95  and EasyChance > 90 :
        CompuResult = user
    else :
        CompuResult = HardGameDict[user]
    OutputDict["CompuResult"] = CompuResult
    OutputDict["Score"] = Score
    return OutputDict

def NormalLevel(usersel):
    CompuResult = 0 
    user = usersel
    Score = 0
    OutputDict = {}
    NormalChance = random.randint(1,100)
    HardGameDict = {1:2,2:3,3:1}
    EasyGameDict = {1:3,2:1,3:2}
    if NormalChance > 50:
        CompuResult = HardGameDict[user]
    elif NormalChance < 50:
        CompuResult = EasyGameDict[user]
        Score += 1
    OutputDict["CompuResult"] = CompuResult
    OutputDict["Score"] = Score
    return OutputDict

def create_database(DatabaseName):
    try:
        myconnection = sqLtor.connect( host = 'localhost' , user = 'root', password = '1234',port="3306")
        cursor = myconnection.cursor()
        cursor.execute(f'CREATE DATABASE IF NOT EXISTS {DatabaseName}')
        myconnection.close()
    except Exception as e:
        print(e)
    
def create_table(TableName,dbs):
    myconnection = sqLtor.connect( host = 'localhost' , user = 'root', password = '1234',port="3306" , database=dbs)
    cursor = myconnection.cursor()
    query = f'''CREATE TABLE IF NOT EXISTS {TableName} (
        LEVEL_SELECTED VARCHAR(10),
        SCORES INT,
        TIMESTAMP DATETIME
    );'''
    cursor.execute(query)
    myconnection.close()

def timestamp_now():
        now = datetime.datetime.now()
        formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
        return formatted_now

def insert_data(TableName,dbs,Value_):
    myconnection = sqLtor.connect( host = 'localhost' , user = 'root', password = '1234',port="3306" , database=dbs)
    cursor = myconnection.cursor()
    query = f"""INSERT INTO {TableName} (LEVEL_SELECTED,SCORES,TIMESTAMP) VALUES(%s
    ,%s,%s)"""
    values = tuple(Value_)
    cursor.execute(query,values)
    myconnection.commit()
    myconnection.close()

def retrive_db_as_df(dbs):
    myconnection = sqLtor.connect( host = 'localhost' , user = 'root', password = '1234',port="3306" , database=dbs)
    query = "SELECT LEVEL_SELECTED , SUM(scores) as Total_Score from history GROUP by level_selected;"
    df = pd.read_sql(query,myconnection)
    return df

def delete_history(tbname , dbs):
    myconnection = sqLtor.connect( host = 'localhost' , user = 'root', password = '1234',port="3306" , database=dbs)
    cursor = myconnection.cursor()
    query = f"TRUNCATE TABLE {tbname}"
    cursor.execute(query)
