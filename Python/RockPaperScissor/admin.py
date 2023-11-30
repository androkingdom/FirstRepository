import function as func

print("==================")
print("Select Choice :-")
print("1 : Score History")
print("2 : Max Played History")
print("3 : Delete History")
print("==================")

choice = int(input("Enter Choice Number : "))

if choice == 1:
    func.graph_Score()
    print(func.df_of_score)

elif choice == 2:
    func.graph_Max_Played()
    print(func.df_of_max_played)

elif choice == 3:
    func.delete_history("history" , "recoreds")
    print("Data Deleted")