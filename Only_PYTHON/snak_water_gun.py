def style(x):
    l = len(x)
    for i in range(l+7):
        print("-",end="")
    print()
    print(f"| => {x} |")
    l = len(x)
    for i in range(l+7):
        print("-",end="")
    print()

def rule():
    print("Snake vs. Water: Snake drinks the water hence wins.")
    print("Water vs. Gun: The gun will drown in water, hence a point for water.")
    print("Gun vs. Snake: Gun will kill the snake and win.")
    print()
    print("** Enter Only In Capital Case **")
    print("!! Type [C] for command !!\n")

def command():
    print("Enter :-")
    print("** Enter Only In Capital Case **")
    print("[S] for Snake")
    print("[W] for Water")
    print("[G] for Gun")
    print("!! Type [O] for Start !!\n")

import random as rn

def comp():
    global coman
    global rn_key
    coman = {"S":"Snake","W":"Water","G":"Gun"}
    rn_key = rn.choice(["S","W","G"])
    rn_val = coman[rn_key]
    return rn_val

chance = 10
points = 0

print("Enter [R] for rule")

while True:
    if chance == 0:
        break
    your_choice = input("Enter => ") # user input
    match your_choice:
                case "R" : rule()            
                case "C" : command()
                case "O" : style("Game Started")
                case _ : style("Invalid command")
    if your_choice == "O":
        while chance >= 1 :
            bot = comp()
            try:
                word = input("Enter Your Choice : ")
                style(f"Your Chance : {chance}")
                word2 = rn_key
                cho = word.capitalize()
                choice = coman[cho]
                style(choice)
                style(bot)
                # for draw 
                if word2 == word:
                    print("Draw")
                    chance -= 1
                # for snake
                elif word == "S" or word == "s" and word2 == "W":
                    print("YOU WINS")
                    points += 1
                    chance -= 1
                elif word == "S" or word == "s" and word2 == "G":
                    print("YOU LOSE")
                    chance -= 1
                # for water  
                elif word == "W" or word == "w" and word2 == "G":
                    print("YOU WINS")
                    points += 1
                    chance -= 1
                elif word == "W" or word == "w" and word2 == "S":
                    print("YOU LOSE")
                    chance -= 1
                # for gun
                elif word == "G" or word == "g" and word2 == "S":
                    print("YOU WINS")
                    points += 1
                    chance -= 1
                elif word == "G" or word == "g" and word2 == "W":
                    print("YOU LOSE")
                    chance -= 1
            except:
                style("Invalid Input!!")
                continue
print(f"Your points : {points}")
            # -------------------------------------------------------