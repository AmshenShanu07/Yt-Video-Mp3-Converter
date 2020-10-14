import youtube_dl
import sys
import os
import time
print("\033[1;32;40m")
os.system('clear')
time.sleep(2)
print (" YOUTUBE VIDEO TO MP3 CONVERTER ")
print ("########################################")
time.sleep(3)
print ( "_______________________________ " )
print ( "|  Coded by H3LL0-H4CK3R       |" )
print ( "|  Thanks for using my tool    |" )
print ( "|______________________________|" )
time.sleep(3)
print("\033[1;33;40m ")
print("###################################")
print("\033[1;34;40m")
time.sleep(3)
print("PROGRAM STARTED")
time.sleep(3)
print("Please Wait")
print("\033[1;31;40m")
time.sleep(2.5)
def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor
spinner = spinning_cursor()
for _ in range(50):
    sys.stdout.write(next(spinner))
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write('\b')
time.sleep(3.5)
print("\033[1;32;40m")
time.sleep(3)
print("###################################")
print("\033[1;36;40m")
time.sleep(3)
print("YOU CAN CONVERT YOUTUBE VIDEOS TO MP3  WITH MY TOOL ")
print("\033[1;31;40m")
time.sleep(3)
print("###################################")
print("\033[1;32;40m")
time.sleep(3)
link = input("Enter Your Link Here :  ")
print("\033[1;36;40m")
print ("Please wait")
time.sleep(2)
print("Converting...")

params ={
    'format': 'bestaudio/best',
    'postprocessors':[{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'MP3',
        'preferredquality': '192',
    }],
    
}

youtube= youtube_dl.YoutubeDL(params)
youtube.download([link])
time.sleep(2.5)
print (" VIDEO TO MP3 CONVERTED SUCCESSFULLY ")
time.sleep(2)
print ("PROGRAM FINISHED ")

