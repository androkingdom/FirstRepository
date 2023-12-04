import random

def SecretCodeGen():
    Code = ""
    number_list = [str(i) for i in range(1,10)]
    for Digit in range(4):
        Number = random.choice(number_list)
        IndexOfNumber = number_list.index(Number)
        Code += Number
        RemoveNumber = number_list.pop(IndexOfNumber)
    return Code

def dict_maker(strtodic):
    create_dict = {}
    key = 1
    for i in strtodic:
        create_dict[key] = i
        key += 1
    return create_dict

def bull_and_cow(scode,gcode):
    bulls = 0
    cows = 0
    scode_dict = dict_maker(scode)
    gcode_dict = dict_maker(gcode)

    if len(scode_dict) != len(gcode_dict):
        return f"length of secret code : {len(scode_dict)}"
    
    for i in scode_dict:
        for j in gcode_dict:
            if scode_dict[i] == gcode_dict[j]:
                if i == j:
                    bulls += 1
                elif i != j:
                    cows += 1

    return {"bull" : bulls , "cow" : cows}

SecretCode = SecretCodeGen()

print("----------Game Started----------")
Guesser = input("Guess Code : ")
BulCowDict = bull_and_cow(SecretCode,Guesser)

if len(Guesser) != 4:
    print(f"Code Length : {len(SecretCode)}")
    
for BullCow in BulCowDict:
    print(f"{BullCow} : {BulCowDict[BullCow]}")

while Guesser != SecretCode:
    Guesser = input("Guess Code : ")
    BulCowDict = bull_and_cow(SecretCode,Guesser)


    for BullCow in BulCowDict:
        print(f"{BullCow} : {BulCowDict[BullCow]}")

print("Code Broken!!")
print(f"Code --> {SecretCode}")