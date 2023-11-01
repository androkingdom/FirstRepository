import pandas as pd
df = pd.read_csv("C:\\Users\\andro\\OneDrive\\Desktop\\MYPROJECTS\\IP Project\\user.csv", names=[
                 "UserName", "LoginId"])

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
    global df
    for row in df.itertuples():
        lst_of_data = list(row)
        if lst_of_data[1] == matchcase:
            return False

# Function - 2 ==> This Function Login Using UserName And LoginID
def login(UserName,LoginID):
    global df
    for i in df.itertuples():
        if UserName == i[1] and LoginID == i[2]:
            return True

login('root',34)