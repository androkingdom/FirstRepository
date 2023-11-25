import style
import random

def result(usersel , compu):
    if usersel not in dic:
        print("Your : Enter Invaild Input")

    elif compu not in dic:
        print("Comp. : Enter Invaild Input")

    else:
        print()
        user = dic[usersel]
        result = user[compu]
        print(f"Your : {meaning[usersel]}")
        print(f"Comp. : {meaning[compu]}")
        style.style(f"Result : {result}")

# rock --> paper
# paper --> scissor
# scissor --> rock

def hard(usersel):

    pass
print("-------------------------")   #Seprator
# tml
# Level Selection

LevelDict = {1:"Hard",2:"Easy",3:"Normal"}

for level in LevelDict:
    print(f"{level} : {LevelDict[level]}")
print()

level_selection = int(input("Enter Level Number : "))
print()

chances = random.choice([i for i in range(1,11)])

dic = {1:{2:"loss",3:"won",1:"draw"},
2:{3:"loss",1:"won",2:"draw"},
3:{1:"loss",2:"won",3:"draw"}}

meaning = {1:"Rock",2:"Paper",3:"Scissor"}
print(chances)

print('''1 --> Rock
2 --> Paper
3 --> Scissors''')
print()

match level_selection :
    case 1:
        print("You have selected Hard Level")
        print("===================")
        if chances <= 8 and chances > 5 :
            selection = int(input("Enter Choice Number: "))
            comp = random.randrange(1,4)
            result(selection,comp)

    case 2:
        print("You have selected Easy Level")
        print("===================")
        if chances == 1 :
            selection = int(input("Enter Choice Number: "))
            comp = random.randrange(1,4)
            result(selection,comp)

    case 3:
        print("You have selected Normal Level")
        print("===================")
        selection = int(input("Enter Choice Number: "))
        comp = random.randrange(1,4)
        result(selection,comp)



# 1 --> Rock
# 2 --> Paper
# 3 --> Scissors