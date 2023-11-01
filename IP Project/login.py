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
    while True:
        print(":---------- Enter ----------:")
        print("1 : Login")
        print("2 : SignUp")
        print("3 : Exit")
        print()
        choice = int(input("Enter your choice : "))
        match choice:
            case 1:
                print("+---------------------+")
                print("|       LoginID       |")
                print("+---------------------+")

                User_Name = input("Enter User Name : ")
                Login_Id = input("Enter LoginId : ")
                CheckName = fn.login(User_Name,Login_Id)
                if CheckName == True:
                    print("Successfully Logined")
                    print()
                    import main 
                    
                else:
                    print("Wrong LoginID or UserName")
            case 2:
                print("+--------------------+")
                print("|       SignUp       |")
                print("+--------------------+")

                UserName = input("Enter User Name : ")
                LoginId = fn.LoginId()

                if fn.unique(UserName) != False:
                    print(f"Your LoginId : {LoginId}")
                    with open("C:\\Users\\andro\\OneDrive\\Desktop\\MYPROJECTS\\IP Project\\user.csv", "at") as file:
                        file.write(f"{UserName},{LoginId}\n")
                else:
                    print("Enter Another Name !!!")
            case 3:
                break
            case _ :
                print("Worng Option!!")

except Exception as e:
    print(e)
