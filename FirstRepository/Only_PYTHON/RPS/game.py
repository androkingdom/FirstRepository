from style import style 
import random

# 1 --> Rock
# 2 --> Paper
# 3 --> Scissors

print('''1 --> Rock
2 --> Paper
3 --> Scissors''')

dic = {1:{2:"loss",3:"won",1:"draw"},
2:{3:"loss",1:"won",2:"draw"},
3:{1:"loss",2:"won",3:"draw"}}

meaning = {1:"Rock",2:"Paper",3:"Scissor"}

a = int(input("Enter : "))
b = random.randrange(1,5)

if a not in dic:
    print("Your : Enter Invaild Input")

elif b not in dic:
    print("Comp. : Enter Invaild Input")

else:
    print()
    user = dic[a]
    result = user[b]
    print(f"Your : {meaning[a]}")
    print(f"Comp. : {meaning[b]}")
    style(f"Result : {result}")