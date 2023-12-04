# Library To Be Used
import random

# Global Variable
Code = ""
Bulls = 0
Cows = 0
Guesser = ""
Score = 0

# Functions To Be Used :-
# Function-1
def ForDigitCode():
    global Code
    number_list = [str(i) for i in range(1,10)]
    for digit_used in range(4):
        digit = random.choice(number_list)
        Code += digit
        number_list.remove(digit)

# Function-2
def BullAndCow(GuessCode , SecretCode):
    global Bulls
    global Cows
    Bulls = 0
    Cows = 0
    list_of_secret_code = list(SecretCode)
    list_of_guess_code = list(GuessCode)
    for secret_code_digit in list_of_secret_code:
        for guess_code_digit in list_of_guess_code:
            if secret_code_digit == guess_code_digit:
                if list_of_secret_code.index(secret_code_digit) == list_of_guess_code.index(guess_code_digit):
                    Bulls += 1
                else:
                    Cows += 1
# Function-3
def IsRepeted(ListOfGuessCode:list ) -> list:
    SetOfCode = set(ListOfGuessCode)
    if len(SetOfCode) < len(ListOfGuessCode) :
        return True

# Working :-
ForDigitCode() # Function Call To Generate Code

print("-----------Game Started-----------")
while Guesser != Code:
    Guesser = input("Guess Code : ")
    if IsRepeted(list(Guesser)):
        print("Duplicate Number Not Allowed")
        continue
    elif len(Guesser) != 4:
        print("Please Enter Four Digits Only")
        continue

    BullAndCow(Guesser , Code)
    Score += 1
    print(f"Bull : {Bulls}\nCow : {Cows}")
    print("=================")

print(f"Code Broken --> {Code}")