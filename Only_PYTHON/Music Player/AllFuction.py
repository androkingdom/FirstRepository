def mytimer(lim):
    import time
    a = 0
    while a < lim:
        a += 1
        time.sleep(1)

def player(location):
    from pygame import mixer
    mixer.init()
    mixer.music.load(location)
    mixer.music.set_volume(0.7)
    mixer.music.play()
    print("Playing....")
    print("Enter 'e' to stop\nEnetr 'p' to pause\nEnter 'r' to resume")
    while True:
        stopper = input("Enter : ")
        if stopper == 'e':
            mixer.music.stop()
            break 
        elif stopper == 'p':
            mixer.music.pause()
            print("Music Paused")
        elif stopper == 'r':
            mixer.music.play()
            print("Music Resumed")
        else:
            print("Some error ocurred")
    