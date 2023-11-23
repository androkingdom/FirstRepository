# ----------------------
import os
import function as fnc
from mutagen.mp3 import MP3
import threading
# ----------------------


# ++++++++++++++++++++++++++++++++++++
sca = os.scandir("musics")
song_dict = {}
file_number = 1
# ++++++++++++++++++++++++++++++++++++

print()
print("==============================================")

for i in sca :
    song_dict[file_number] = (i.name)
    print(f"{file_number} : {song_dict[file_number]}")
    file_number += 1

print("==============================================")

SongNumber = int(input("Select Song Number : "))
music_loc = f"musics\\{song_dict[SongNumber]}"
music = MP3(music_loc)
Length_Of_Music = int(music.info.length)
fnc.style1(song_dict[SongNumber],"Song Name => ")
fnc.style1(f"{Length_Of_Music}","Length Of Music => ","sec")

print("==============================================")

t1 = threading.Thread(target=fnc.player,args=(music_loc,))
t2 = threading.Thread(target=fnc.timer,args=(Length_Of_Music,))

t1.start()
t2.start()

t1.join()
t2.join()