import os
choice = input("Do wo allow to make file : ")
if choice == "yes" or choice == "Yes": 
    try:
        os.mkdir("Detail")
        with open("Detail/Det.txt","w") as f:
            f.read()
    except:
        print("Created a new file")
    print("ENTER")
    print("1. TO ENTER DATA")
    print("2. TO REVIRT DATA")
    choice2 = int(input("==> "))
    if choice2 == 1:
        data = input("Enter data : ")
        with open("Detail/Det.txt","wt") as f:
            f.write(f"{data}")
    elif choice2 == 2:
        with open("Detail/Det.txt","r") as f:
            print(f.read())
else :
    print("Please allow permission")