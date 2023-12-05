# Library Used
import random


# Variable Used
words = '''ant baboon badger bat bear beaver camel cat clam cobra cougar
       coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
       lion lizard llama mole monkey moose mouse mule newt otter owl panda
       parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
       skunk sloth snake spider stork swan tiger toad trout turkey turtle
       weasel whale wolf wombat zebra'''.split()

words_list = list(words)
getword = random.choice(words_list)
list_of_cover = []
list_of_getword = list(getword)
uncovering_word = "".join(list_of_cover)
chance_to_uncover = 0

# Functio To Be Used
def covers():
    global getword
    for i in range(len(getword)):
        list_of_cover.append("_")

def change_covers(x = ""):
    global list_of_cover, list_of_getword, uncovering_word
    # if x not in list_of_getword:
    #     print("Not a Letter")
    # elif x in list_of_getword:
    #     print("Letter Founded")

    for i in list_of_getword:
        if i == x:
            indx = list_of_getword.index(i)
            list_of_cover[indx] = x
            list_of_getword[indx] = ""
    uncovering_word = "".join(list_of_cover)

def alert(x):
    global list_of_cover, list_of_getword, uncovering_word
    if x not in list_of_getword:
        print("==============")
        print("Not a Letter")
        print("==============")
    elif x in list_of_getword:
        print("==============")
        print("Letter Founded")
        print("==============")

# Working :-
covers()
change_covers()
print("=========================")
print("Welcome To HangMan Game")
print("=========================")
while uncovering_word != getword:
    print(uncovering_word , end=" ")
    letter = input("Enter a Letter : ")
    if len(letter) != 1:
        print("!! You Are Disqualified To Enter More Than One Letter !!")
        break
    chance_to_uncover += 1
    change_covers(letter)
    alert(letter)

if uncovering_word == getword:
    print("Your find the word")
    print(f"You Won The Game In {chance_to_uncover} Chance")