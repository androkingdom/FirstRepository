import pandas as pd
import mysql.connector as sqLtor
import Function as fn

connection = sqLtor.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="project"
)

print(f"Connection Status : {connection.is_connected()}")

try:
    print(":---------- Enter ----------:")
    print("1 : Login")
    print("2 : Signup")
    print()
    choice = int(input("Enter your choice : "))
    match choice:
        case 1:
            UserName = input("Enter User Name : ")
            LoginId = input("Enter LoginId : ")
            df = pd.read_csv("C:\\Users\\andro\\OneDrive\\Desktop\\MYPROJECTS\\IP Project\\user.csv", names=[
                 "UserName", "LoginId"])
            # for 

        case 2:
            UserName = input("Enter User Name : ")
            LoginId = fn.LoginId()

            if fn.unique(UserName) != False:
                print(f"Your LoginId : {LoginId}")
                with open("C:\\Users\\andro\\OneDrive\\Desktop\\MYPROJECTS\\IP Project\\user.csv", "at") as file:
                    file.write(f"{UserName},{LoginId}\n")
            else:
                print("Enter Another Name !!!")

except Exception as e:
    print(e)
