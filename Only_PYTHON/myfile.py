# a = {1,2,3,4,5,6}
# b = {1,74,7,3,23,2,32}
# c = {38,48,347,3}
# print(a)
# print(b)
# print(c)

# for i in range(6,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# print("I have done it !!")

# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# b = 1
# while b <= 10:
#     a = 1 
#     for i in range(b):
#         print(a,end=" ")
#         a += 1
#     b += 1
#     print()

# a = 0
# b = 0
# for i in range(5):
#     for j in range(b):
#         print(a,end=" ")
#         a += 1
#     b += 1
#     print()

# def style(x):
#     l = len(x)
#     for i in range(l+7):
#         print("-",end="")
#     print()
#     print(f"| => {x} |")
#     l = len(x)
#     for i in range(l+7):
#         print("-",end="")
#     print()

import random as rn
def comp():
    global coman
    coman = {"S":"Snake","W":"Water","G":"Gun"}
    rn_key = rn.choice(["S","W","G"])
    rn_val = coman[rn_key]
    return rn_val
while True:
    bot = comp()
    print(bot)