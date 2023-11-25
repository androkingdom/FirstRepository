def style1(x,y,z=""):
    length = len(x) + 10 + len(y) +len(z)
    for i in range(length):
        print("=",end="")
    print(f"\n|{y}    {x}    {z}|")
    for i in range(length):
        print("=",end="")
    print()


def player(song_location):
    from pygame import mixer
    mixer.init()
    mixer.music.load(song_location)
    mixer.music.set_volume(10)
    mixer.music.play()

def timer(howmuch):
    import time
    for sec in range(howmuch + 1):
        print(f"{sec} / {howmuch} \r",end="")
        time.sleep(1)
