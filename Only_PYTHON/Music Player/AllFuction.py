def mytimer(lim):
    import time
    a = 0
    while a < lim:
        a += 1
        time.sleep(1)

def timeplayer(location):
    from pygame import mixer
    mixer.init()
    mixer.music.load(location)
    mixer.music.set_volume(0.7)
    mixer.music.play()
   
    stopper = input("Enter 'e' to stop : ")
    if stopper == 'e':
        mixer.music.stop()
            
    else:
        print("Some error ocurred")
    