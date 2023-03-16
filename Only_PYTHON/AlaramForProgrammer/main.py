import time
import pyttsx3
import os
from pygame import mixer
engine = pyttsx3.init()

use = "Timer For : "

def useoftimer(x):
    with open("all_alram_records.txt","w") as fileo:
        fileo.write(x)

lis = ["M","H","S"]
dic = {"M":60,"H":60*60,"S":1}

engine.setProperty('rate',145)
engine.say("Sir! Enter , M For Minute , H For Hour ,And, S For Second")
engine.runAndWait()

tim = input("Enter : ")
timer = tim.upper()
if timer not in lis:
    print("Wrong Input")
    raise ValueError

else:
    use+=timer
    engine.say("Sir! Enter , Time!")
    engine.runAndWait()
    timing = int(input("Enter : "))
    RealTime = dic[timer]*timing
    use+=str(timing)
    useoftimer(use)
    print("Time Started !!")
    for i in range(RealTime):
        time.sleep(1)
    
engine.say("Sir! Timer Is Stoped!!")
engine.runAndWait()
os.remove("all_alram_records.txt")

mixer.init()
mixer.music.load("Only_PYTHON\\AlaramForProgrammer\\download.mp3")
mixer.music.set_volume(0.7)
mixer.music.play()