# enter choice : Eve
# enter number : 1 - 10
# your : [enter number]
# bot : [bot number]

# Values:-
# Player --> 1
# Bot --> 2

import random as rn

TossWin = 0
BatOrBall = ""

print("Enter [Eve] or [Odd] : ",end="")
check = ["Odd","Eve"]
Player_Choose = input(": ")
if Player_Choose not in check:
    print("Invaild Input !!")

else:
    dic = {"Odd":[1,3,5,7,9,11,13,15,17,19],"Eve":[2,4,6,8,10,12,14,16,18,20]}
    PlayerNumber =  int(input("Enter Number Between 1 - 10 : "))
    RandomNumber = rn.randint(1,10)
    print(f"Your : {PlayerNumber}")
    print(f"Bot : {RandomNumber}")
    sm = PlayerNumber + RandomNumber
    Player = dic[Player_Choose]
    if sm in Player:
        print("You choose [Bat] or [Ball]",end="")
        TossWin = 1
    else:
        print("Bot choosing [Bat] or [Ball] : ",end="")
        TossWin = 2

def UserBat():
    PlayerPoints = 0
    BotPoints = 0
    PlayerScore = int(input("Enter Number : "))
    BotScore = rn.randint(1,10)
    while PlayerScore != BotScore :
        PlayerPoints += PlayerScore
        Plyr = PlayerBat(PlayerScore,BotScore)
        PlayerScore = int(input("Enter Number : "))
        BotScore = rn.randint(1,10)
    if PlayerScore == BotScore:
        print("You Bowled")
        print(f"Your Total Points : {PlayerPoints}")
        print("Now Your Balling")
        BotBat()

def BotBat():
    PlayerPoints = 0
    BotPoints = 0
    PlayerScore = int(input("Enter Number : "))
    BotScore = rn.randint(1,10)
    while BotScore != PlayerScore :
        BotPoints += BotScore
        Plyr = PlayerBat(PlayerScore,BotScore)
        PlayerScore = int(input("Enter Number : "))
        BotScore = rn.randint(1,10)
    if PlayerScore == BotScore:
        print("Bot Bowled")
        print(f"Bots Total Points : {BotPoints}")
        print("Now Your Batting")
        UserBat()

class PlayerBat:
    def __init__(self,Number1,Numebr2):
        self.n1 = Number1
        self.n2 = Numebr2
        print(f"Your Number => {self.n1}")
        print(f"Bot Number => {self.n2}")

if TossWin == 1:
    BatOrBall = input(": ")

if BatOrBall == "Bat":
    UserBat()
elif BatOrBall == "Ball":
    BotBat()

elif TossWin ==2:
    BatOrBall = rn.choice(["Bat","Ball"])
    print(BatOrBall)

if BatOrBall == "Bat":
    BotBat()
elif BatOrBall == "Ball":
    UserBat()