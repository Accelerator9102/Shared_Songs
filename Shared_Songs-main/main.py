import get_library
import os
import time
import webbrowser
import get_tracks

spo1 = get_library.get_library("6f874370eddc4801884f78e2720ec458", "d62e26bff1d94f79abbd43c38e81a210",
                               "http://localhost:9999/callback")

webbrowser.open("https://www.spotify.com/ca-en/logout/")

os.remove(".cache")
time.sleep(5)

spo2 = get_library.get_library("e8964862d98e46be8517aca483e34f81", "ae0443350a954049816fd3ee4025ad19",
                               "http://localhost:1000/callback")
os.remove(".cache")
webbrowser.open("https://www.spotify.com/ca-en/logout/")

# print(spo1)
# print(spo2)
shorter_set = set()
longer_set = set()

if len(spo1) <= len(spo2):
    shorter_set = spo1
    longer_set = spo2

else:
    shorter_set = spo2
    longer_set = spo1

same_set = set()
for track in shorter_set:
    if track in longer_set:
        same_set.add(track)

list_track = get_tracks.get_tracks(same_set)

with open('song_list.txt', 'w',encoding="utf-8") as f:
    for el in list_track:
        f.write("%s\n" % el)

os.path.abspath("../index.html")

webbrowser.open("file://" + os.path.abspath("../index.html"))

# for el in list_track:
#    print(el)
