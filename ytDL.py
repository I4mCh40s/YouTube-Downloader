from pytube import YouTube
import time

link = input("Video link: ")

yt = YouTube(link)

vd = yt.streams.get_highest_resolution()

folder = input("Destination folder: ")

try:
    vd.download(folder)
except:
    print("Oops... smth went wrong. Big sad :'(")
else:
    print("Success! ", yt.title, " video with ", yt.views, "views is downloaded!")
    print("Find it here: ", folder)

time.sleep(5)
