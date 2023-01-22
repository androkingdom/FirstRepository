import random as rn
chance = 10

def style(x):
    print("---------")
    print(f"    {x}")
    print("---------")

def rule():
    print("Snake vs. Water: Snake drinks the water hence wins.")
    print("Water vs. Gun: The gun will drown in water, hence a point for water.")
    print("Gun vs. Snake: Gun will kill the snake and win.")
    print("!! Type [C] for command")

def command():
    print("Enter :-")
    print("1. for Snake")
    print("2. for Water")
    print("3. for Gun")

print("Enter [R] for rule")
while chance >= 1 :
    your_choice = input("Enter => ")
    style(your_choice)
    match your_choice:
        case "R" : rule()
        case "r" : rule()
        case "c" : command()
        case "C" : command()
