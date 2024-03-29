import function as func
import pandas as pd

print("-------------------------")   #Seprator

# Level Selection

LevelDict = {1:"Hard",2:"Easy",3:"Normal"}

for level in LevelDict:
    print(f"{level} : {LevelDict[level]}")
print()

level_selection = int(input("Enter Level Number : "))
print()

NumberOfRound = int(input("Enter Number Of Round : "))

print('1 --> Rock \n2 --> Paper \n3 --> Scissors')
print()

NetScore = 0
HistoryDict = {}
CurrentTime = func.timestamp_now()

try:
    for RoundNumber in range(NumberOfRound):
        print("=================")
        print(f"Round - {RoundNumber + 1}")
        print("=================")
        match level_selection :
            case 1:
                print("============================")
                print("You have selected Hard Level")
                print("============================")
                selection = int(input("Enter Choice Number: "))
                ResultingDict = func.HardLevel(selection)
                comp = ResultingDict["CompuResult"]
                NetScore += ResultingDict["Score"]
                func.result(selection,comp)

            case 2:
                print("============================")
                print("You have selected Easy Level")
                print("============================")
                selection = int(input("Enter Choice Number: "))
                ResultingDict = func.EasyLevel(selection)
                comp = ResultingDict["CompuResult"]
                NetScore += ResultingDict["Score"]
                func.result(selection,comp)

            case 3:
                print("==============================")
                print("You have selected Normal Level")
                print("==============================")
                selection = int(input("Enter Choice Number: "))
                ResultingDict = func.NormalLevel(selection)
                comp = ResultingDict["CompuResult"]
                NetScore += ResultingDict["Score"]
                func.result(selection,comp)

    print(f"Net Score => {NetScore}")
    
    Lebel = LevelDict[level_selection]
    HistoryDict["Level Selected"] = (Lebel)
    HistoryDict["Score"] = (NetScore)
    HistoryDict["TimeStamp"] = (CurrentTime)

except Exception as e:
    print(e)
func.create_database("Recoreds")
func.create_table("History","Recoreds")
func.insert_data("History","Recoreds",list(HistoryDict.values()))