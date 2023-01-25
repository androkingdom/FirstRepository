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