import function as func

print("==================")
print("Select Choice :-")
print("1 : Score History")
print("2 : Max Played History")
print("==================")

choice = int(input("Enter Choice Number : "))

if choice == 1:
    # print("==================")
    # print("1 : Graph View")
    # print("2 : Database View")
    # print("==================")
    # choice_inside = int(input("Enter Choice Number : "))
    # match choice_inside:
        # case 1 :
    func.graph_Score()
        # case 2 : 
    print(func.df_of_score)

elif choice == 2:
    # print("==================")
    # print("1 : Graph View")
    # print("2 : Database View")
    # print("==================")
    # choice_inside = int(input("Enter Choice Number : "))
    # match choice_inside:
        # case 1 :
    func.graph_Max_Played()
        # case 2 : 
    print(func.df_of_max_played)