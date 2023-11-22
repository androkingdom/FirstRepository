# all working module and file
import func
from threading import Thread

location = f"music" 
dic_of_folder = func.file_dic_infolder
func.list_maker(location)
while True:
    print("\nEnter which song number you want to play")
    song_will_be = int(input("Enter : "))

    print()

    song_to_played = dic_of_folder[song_will_be]
    music_loc = f"{location}\\{song_to_played}"
    time_of_music = func.time_teller(music_loc)
    print(f"Music - {song_to_played}")
    print()
    t1 = Thread(target=func.playmusic,args=[music_loc])


    t1.start()
    
    t1.join()