import AllFuction as ch
import os

working_dir = os.chdir("C:\\Users\\andro\\OneDrive\\Desktop\\My_Projects\\Only_PYTHON\\Music Player\\Musics-for-program")
music_lst = os.listdir(working_dir)
music_dic = {}
music_no = 1
Good = True

while Good:
    for songs in music_lst:
        song_name = songs.replace(".mp3","")
        print(f"{music_no} : {song_name}")
        music_dic[music_no] = songs
        music_no += 1
    
    print()

    user_song = int(input("Enter Song Number : "))
    print("Playing....")
    print(f"Music - {music_dic[user_song]}")
    loc = f"{music_dic[user_song]}"
    ch.timeplayer(loc)
    print("Enter \"q\" to stop Player\nEnter \"a\" for play another song")
    query = input("Enter : ")
    if query == "q":
        Good = False
    elif query == "a":
        music_no = 1

print("Player Closed")