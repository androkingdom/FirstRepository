import random

print("1.Coding")
print("2.Decoding")
choice = int(input("Enter 1 for Coding and 2 for Decoding : "))
if choice == 1:
    alpha_lst = ["a","v","e","n","x","i","y","d"]

    r1 = random.choice(alpha_lst)
    r2 = random.choice(alpha_lst)
    r3 = random.choice(alpha_lst)
    r4 = random.choice(alpha_lst)
    r5 = random.choice(alpha_lst)
    r6 = random.choice(alpha_lst)


    word = input("Enter the word : ")
    code_word = ""
    word_lst = list(word)
    lth = len(word_lst)

    if lth < 3 :
        new_lst = word_lst[::-1]
        code_word = "".join(new_lst)
        print(f"code word {code_word}")

    elif lth >= 3 :
        a1 = word_lst.pop(0)
        c1 = "".join(word_lst)
        c2 = r1+r2+r3+c1+a1+r4+r5+r6
        code_word = c2
        print(f"code word : {code_word}")

elif choice == 2:
    code_word = input("Enter the word : ")
    word = ""
    word_lst = list(code_word)
    lth = len(word_lst)

    if lth < 3 :
        new_lst = word_lst[::-1]
        word = "".join(new_lst)
        print(f"word : {word}")
        
    elif lth >= 3 :
        a1 = word_lst.pop(-4)
        stat_word = word_lst[3:]
        d1 = stat_word.pop(-1)
        d2 = stat_word.pop(-1)
        d3 = stat_word.pop(-1)
        print(stat_word)
        c1 = a1 + "".join(stat_word)
        word = c1
        print(f"word : {word}")