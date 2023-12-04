import random

def SecretCodeGen():
    try:    
        Code = ""
        number_list = [str(i) for i in range(1,10)]
        for Digit in range(4):
            IndexOfNumber = number_list.index(random.choice(number_list))
            RemoveNumber = number_list.pop(IndexOfNumber)
            Code += RemoveNumber
        return Code
    except Exception as e:
        print(e)


# def dict_maker(strtodic):
#     create_dict = {}
#     key = 1
#     for i in strtodic:
#         create_dict[key] = i
#         key += 1
# return create_dict

def bull_and_cow(scode,gcode):
    try:
        bulls = 0
        cows = 0
        lst_scode = list(scode)
        lst_gcode = list(gcode)

        if len(lst_scode) != len(lst_gcode):
            return f"length of secret code : {len(lst_scode)}"

        for i in lst_scode:
            for j in lst_gcode:
                if lst_scode.index(i) == lst_gcode.index(j):
                    if i == j:
                        bulls += 1
                    elif i != j:
                        cows += 1

        return {"bull" : bulls , "cow" : cows}
    except Exception as e:
        print(e)

SecretCode = SecretCodeGen()
print(SecretCode)

print("----------Game Started----------")
Guesser = input("Guess Code : ")
BulCowDict = bull_and_cow(SecretCode,Guesser)

try:
    if len(Guesser) != 4:
        print(f"Code Length : {len(SecretCode)}")
        
    for BullCow in BulCowDict:
        print(f"{BullCow} : {BulCowDict[BullCow]}")
except Exception as e:
    print(e)

while Guesser != SecretCode:
    try:
        print("=========================")
        Guesser = input("Guess Code : ")
        BulCowDict = bull_and_cow(SecretCode,Guesser)


        for BullCow in BulCowDict:
            print(f"{BullCow} : {BulCowDict[BullCow]}")
    except Exception as e:
        print(e)
        continue

print("Code Broken!!")
print(f"Code --> {SecretCode}")