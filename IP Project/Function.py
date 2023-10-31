# Function - 1 ==> This Function Create Login Id
import pandas as pd


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
df = pd.read_csv("C:\\Users\\andro\\OneDrive\\Desktop\\MYPROJECTS\\IP Project\\user.csv", names=[
                 "UserName", "LoginId"])


def unique(matchcase):
    for row in df.itertuples():
        lst_of_data = list(row)
        if lst_of_data[1] == matchcase:
            return False
