import pandas as pd
import mysql.connector as sqLtor
import Function as fn


if __name__ == "__main__":
    fn.create_database()

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

                    if fn.CsvIsEmpty() == True:
                        print("!!!No One Is Login!!!")
                        print("!!!Please First Login!!!")
                        
                    else:
                        User_Name1 = input("Enter User Name : ")
                        User_Name = User_Name1.replace(" ","")

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

                    UserName1 = input("Enter User Name : ")
                    UserName = UserName1.replace(" ","")
                    LoginId = fn.LoginId()
                    
                    if fn.AlphaInUserName(UserName) == True:
                        if fn.unique_(UserName) != False:
                            print(f"Your LoginId : {LoginId}")
                            with open("C:\\Users\\andro\\OneDrive\\Desktop\\MYPROJECTS\\IP Project\\user.csv", "at") as file:
                                file.write(f"{UserName},{LoginId}\n")
                        else:
                            print("Enter Another Name !!!")
                    else:
                        print("User Cannot Be Assign")
                case 3:
                    break
                case _ :
                    print("Worng Option!!")

    except Exception as e:
        print(e)
