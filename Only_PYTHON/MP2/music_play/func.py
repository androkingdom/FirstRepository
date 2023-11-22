# All Laibrary Used
from pygame import mixer
from time import sleep
from mutagen.mp3 import MP3
import os

# All Varibale Used
working_dir = os.getcwd()
file_number = 1
file_dic_infolder = {}
file = ""
list_of_files = []
approx_audio_length = 0
working = True
choice = ""
length_of_music = 0

# All Function

# ---> music player(audio player)
def playmusic(loc):
    global choice
    global working
    global length_of_music
    mixer.init()
    mixer.music.load(loc)
    length_of_music = mixer.Sound(loc)
    print("length - ",length_of_music.get_length())
    mixer.music.set_volume(10)
    mixer.music.play()
    print('Enter "s" to stop\nEnter "p" to pause\nEnter "r" to resume')
    print()
    while working:
        choice = input("Enter : ")
        match choice:
            case "s" : 
                mixer.music.stop()
                break
            case "p" : mixer.music.pause()
            case "r" : mixer.music.unpause()
            case _ : print("Invalid command")

# ---> time taken by audio
def time_teller(audio_loc):
    global approx_audio_length
    audio = MP3(audio_loc)
    audio_length = audio.info.length
    approx_audio_length = int(audio_length)
    return  approx_audio_length

# ---> create list of folder
def list_maker(location_of_folder=working_dir):
    global file_number
    global file_dic_infolder
    global file
    global list_of_files
    list_of_files = os.listdir(location_of_folder)
    for file in list_of_files:
        if file.endswith(".mp3"):
            filename = str(file).replace(".mp3","")
            print(f"{file_number} : {filename}")
            file_dic_infolder[file_number] = file
            file_number += 1

# # ---> create list of folder
# def timer2(time):
#     global count_down
#     for count_down in range(1,time + 1):
#         sleep(1)
