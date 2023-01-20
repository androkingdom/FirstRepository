request_ = input('Enter : ')
while request_ != "/exit":
    first_letter = request_[0]
    if first_letter != "/":
        print("Start command with '/' ")
    else:
        match request_:
            case "/help" :  print("hello!! \nMy name is hybrid\nI am a bot\nYou can exit with '/exit' command")
            case "/calculate" : import calculater as calc
            case "/calcrule" :
                with open("calculater.txt","rt") as f:
                    print(f.read())

# don't write code below this            
    request_ = input('Enter : ')