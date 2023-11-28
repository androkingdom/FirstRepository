# Library Used 
import random
import style
import pandas as pd
import mysql.connector as sqLtor
import datetime
from numpy import random
from sqlalchemy import create_engine
from matplotlib import  pyplot as plt

# Global Variables Used
df_of_score = 0
df_of_max_played = 0

# Give The Result Of Game
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

# Set Game Level To Hard
def HardLevel(usersel):
    CompuResult = 0 
    user = usersel
    Score = 0
    OutputDict = {}
    HardGameDict = {1:2,2:3,3:1}
    EasyGameDict = {1:3,2:1,3:2}
    HardChance = random.randint(1,100)
    if HardChance <= 80 and HardChance >= 1:
        CompuResult = HardGameDict[user]
    elif HardChance < 95  and HardChance > 90 :
        CompuResult = user
    else :
        CompuResult = EasyGameDict[user]
        Score += 1
    OutputDict["CompuResult"] = CompuResult
    OutputDict["Score"] = Score
    return OutputDict

# Set Game Level To Easy
def EasyLevel(usersel):
    CompuResult = 0 
    user = usersel
    Score = 0
    OutputDict = {}
    EasyChance = random.randint(1,100)
    HardGameDict = {1:2,2:3,3:1}
    EasyGameDict = {1:3,2:1,3:2}
    if EasyChance <= 80 and EasyChance >= 1:
        CompuResult = EasyGameDict[user]
        Score += 1
    elif EasyChance < 95  and EasyChance > 90 :
        CompuResult = user
    else :
        CompuResult = HardGameDict[user]
    OutputDict["CompuResult"] = CompuResult
    OutputDict["Score"] = Score
    return OutputDict

# Set Game Level To Normal
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

# Create Database Named Recoreds
def create_database(DatabaseName):
    try:
        myconnection = sqLtor.connect( host = 'localhost' , user = 'root', password = '1234',port="3306")
        cursor = myconnection.cursor()
        cursor.execute(f'CREATE DATABASE IF NOT EXISTS {DatabaseName}')
        myconnection.close()
    except Exception as e:
        print(e)

# Create Tabele Named History To Store Data
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

# To Return TimeStamp When Called
def timestamp_now():
        now = datetime.datetime.now()
        formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
        return formatted_now

# Used To Enter Date To Specific Table
def insert_data(TableName,dbs,Value_):
    try:
        myconnection = sqLtor.connect( host = 'localhost' , user = 'root', password = '1234',port="3306" , database=dbs)
        cursor = myconnection.cursor()
        query = f"""INSERT INTO {TableName} (LEVEL_SELECTED,SCORES,TIMESTAMP) VALUES(%s
        ,%s,%s)"""
        values = tuple(Value_)
        cursor.execute(query,values)
        myconnection.commit()
        myconnection.close()
    except:
        print("You Enter Wrong Input")

# Used To Plot Graph On Score History
def graph_Score():
    global df_of_score
    query2 = '''SELECT LEVEL_SELECTED , SUM(scores) as total_played from history group by level_selected'''
    myconnection = sqLtor.connect( host = 'localhost' , user = 'root', password = '1234',port="3306" , database="recoreds")
    cursor = myconnection.cursor()
    cursor.execute(query2)
    result = cursor.fetchall()
    df1 = pd.DataFrame(result, columns=['Level Selected', 'Score'])
    df_of_score = df1
    plt.bar(df1['Level Selected'], df1['Score'])
    plt.xlabel('Level')
    plt.ylabel('Score')
    plt.title('Score Graph')
    plt.yticks([])
    plt.show()
    myconnection.close()

# Used To Plot Graph On Max Played History
def graph_Max_Played():
    global df_of_max_played
    query1 = '''SELECT LEVEL_SELECTED , COUNT(level_selected) as total_played from history group by level_selected'''
    myconnection = sqLtor.connect( host = 'localhost' , user = 'root', password = '1234',port="3306" , database="recoreds")
    cursor = myconnection.cursor()
    cursor.execute(query1)
    result = cursor.fetchall()
    df1 = pd.DataFrame(result, columns=['Level Selected', 'Total Played'])
    df_of_max_played = df1
    plt.bar(df1['Level Selected'], df1['Total Played'])
    plt.xlabel('Level')
    plt.ylabel('Total Played')
    plt.title('Time Spent Graph')
    plt.yticks([])
    plt.show()
    myconnection.close()

# Used Delete All Recoreds From Table
def delete_history(tbname , dbs):
    myconnection = sqLtor.connect( host = 'localhost' , user = 'root', password = '1234',port="3306" , database=dbs)
    cursor = myconnection.cursor()
    query = f"TRUNCATE TABLE {tbname}"
    cursor.execute(query)
