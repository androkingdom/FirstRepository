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

# a = "a"
# l = ["harry","sam","anshul"]
# for i in l:
#     if a in i:
#         print(i)
#     else:
#         print("not found")

# -x + 1 ,x < 0			|x| = -x , x < 0
# 0 ,x = 0				
# x + 1 ,x > 0			|x| = x , x > 0

# at x = 0:
# 	L.H.L:
# 		lim f(X) = lim -x + 1
# 		x--> 0^-   x--> 0^-
# 				 = 0 + 1
# 				 = 1
# 	!! similary for R.H.L !! 
# Importing urllib request module in the program  


from urllib.request import urlopen
with urlopen("https://open.spotify.com/album/5HwDqY57GHF4LhBvXUrilS") as response:
   html = response.read()