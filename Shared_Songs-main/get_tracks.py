#-------------------------------------------------------------------------------
# NAME:    Spotify Track Info Obtainer 
# PURPOSE: To return a list of track info given id
#
# LAST EDITED BY: Xiaoyu Xie
# LAST EDITED: 21/11/2020
# PURPOSE OF EDIT: Final Version
#-------------------------------------------------------------------------------
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def get_tracks(id_set):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="6f874370eddc4801884f78e2720ec458",
                                                               client_secret="d62e26bff1d94f79abbd43c38e81a210"))
    idx = 1
    list_track = []
    for id in id_set:
        track = sp.track(id)
        string_track = str(idx) +" "+track['artists'][0]['name'] + " – " + track['name']
        print(string_track)
        list_track.append(string_track)
        idx += 1
    return list_track
