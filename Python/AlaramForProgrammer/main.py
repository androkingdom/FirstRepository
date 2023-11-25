import threading
from pygame import mixer
import function  as funct

lis = ["M","H","S"]
dic = {"M":60,"H":60*60,"S":1}
print()
print("----------------------")
print("Sir! Enter \nM For Minute \nH For Hour \nS For Second")
print("----------------------")
tim = input("Enter : ")
timer_ = tim.upper()
try:
    if timer_ not in lis:
        print("Wrong Input")
        raise ValueError
except:
    print("Wrong Command")

else:
    use = "Timer For - "
    use+=timer_
    print("----------------------")
    print("Sir! Enter Time")
    print("----------------------")
    timing = int(input("Enter : "))

    RealTime = dic[timer_]*timing
    use+=str(timing)
    with open("all_alram_records.txt","w") as fileo:
        fileo.write(use)
    try:
        t2 = threading.Thread(target=funct.player,args=(RealTime,))
        t1 = threading.Thread(target=funct.timer, args=(RealTime,))
    
        t1.start()
        t2.start()
    
        t1.join()
        t2.join()
    except:
        print("Error")