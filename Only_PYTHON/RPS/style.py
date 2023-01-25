# ------------
# | =>       |
# ------------
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

#  = = = =
# ||     ||
#  = = = =
def style2(x):
    l = len(x)
    for i in range(l-1):
        print(" =",end="")
    print()
    print(f"||{x}||")
    for i in range(l-1):
        print(" =",end="")

#  _____
# |     |
#  -----
def style3(x):
    l = len(x)
    print(" ",end="")
    for i in range(l):
        print("_",end="")
    print()
    print(f"|{x}|")
    print(" ",end="")
    for i in range(l):
        print("-",end="")

style3("hello")