# Library Used
import random


# Variable Used
words = '''Lion Tiger Leopard Cheetah Elephant Giraffe Rhinoceros Gorilla Chimpanzee Wolf Bear Panda 
            Kangaroo Koala Zebra Hippopotamus Crocodile Alligator Cheetah Bison zebra'''.split()

words_list = list(words)
getword = random.choice(words_list).lower()
list_of_cover = []
list_of_getword = list(getword)
uncovering_word = 0
word_used = []
chance_to_uncover = 0

# Functio To Be Used
def create_covers():
    global getword, uncovering_word
    for i in range(len(getword)):
        list_of_cover.append("_")
    uncovering_word = "".join(list_of_cover)

def change_covers(x):
    global list_of_cover, list_of_getword, uncovering_word
    for i in list_of_getword:
        if i == x:
            indx = list_of_getword.index(i)
            list_of_cover[indx] = x
            list_of_getword[indx] = ""
    uncovering_word = "".join(list_of_cover)

# working
create_covers()

print("==============================================")
print("Welcome To HangMan Game - Living Thing Version")
print("==============================================")
for i in range(7):
    chance_to_uncover += 1
    print(uncovering_word , end=" ")
    letter = input("Guess The Letter : ").lower()
    print()
    if letter in list_of_getword:
        print("You Found A Letter")
    if letter not in list_of_getword:
        print("Wrong Letter")
    print()
    if letter not in word_used:
        word_used.append(letter)
        change_covers(letter)
        if uncovering_word == getword:
            print(f"{uncovering_word} : You Find The Word")
            break
        elif len(letter) != 1:
            print("!! You Are Disqualified To Enter More Than One Letter !!")
            break
    else:
        print("Letter Already Used")

if uncovering_word == getword:
    print(f"You Won The Game In {chance_to_uncover} Chance")
elif uncovering_word != getword:
    print(f"You Loss The Game Correct Word Is {getword}")