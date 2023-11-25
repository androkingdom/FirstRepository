import time
import os
from pygame import mixer

RealTime = 0
def timer(HowMuch):
    for count_down in range(HowMuch + 1):
        print(f"{count_down}/{HowMuch} \r",end="")
        time.sleep(1)
    # print(f"{count_down}/{HowMuch}",end="")    


def player(rtime):
    print("----------------------")
    print("Time Started !!")
    print("----------------------")
    for i in range(rtime):
        time.sleep(1)
    print("----------------------")
    print("Sir! Timer Is Stoped!!")
    print("----------------------")
    os.remove("all_alram_records.txt")
    mixer.init()
    mixer.music.load("download.mp3")
    mixer.music.set_volume(10)
    mixer.music.play()
    print()
    while True:
        try:
            choice = int(input("Press Key To Stop........"))
        except:
            print("Stopped")
            break