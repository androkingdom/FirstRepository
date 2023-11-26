import style
import random

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
                ResultingDict = HardLevel(selection)
                comp = ResultingDict["CompuResult"]
                NetScore += ResultingDict["Score"]
                result(selection,comp)

            case 2:
                print("============================")
                print("You have selected Easy Level")
                print("============================")
                selection = int(input("Enter Choice Number: "))
                ResultingDict = EasyLevel(selection)
                comp = ResultingDict["CompuResult"]
                NetScore += ResultingDict["Score"]
                result(selection,comp)

            case 3:
                print("==============================")
                print("You have selected Normal Level")
                print("==============================")
                selection = int(input("Enter Choice Number: "))
                ResultingDict = NormalLevel(selection)
                comp = ResultingDict["CompuResult"]
                NetScore += ResultingDict["Score"]
                result(selection,comp)

    print(f"Net Score => {NetScore}")
except Exception as e:
    print(e)