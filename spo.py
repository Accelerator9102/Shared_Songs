import spotipy
from spotipy.oauth2 import SpotifyOAuth


def get_library(client_id, client_secret, red_uri):
    MAX_SIZE = 50
    spo = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                    client_secret=client_secret,
                                                    redirect_uri=red_uri,
                                                    scope="user-library-read"))

    flag = True
    start = 0
    list_of_track_id1 = set()
    results = spo.current_user_saved_tracks(limit=MAX_SIZE, offset=start)

    if len(results['items']) < 50:
        flag = False
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], " – ", track['name'])
        list_of_track_id1.add(track['id'])

    while flag:
        start += MAX_SIZE
        results = spo.current_user_saved_tracks(limit=MAX_SIZE, offset=start)

        if len(results['items']) == 0:
            flag = False
        for idx, item in enumerate(results['items'], start=start):
            track = item['track']
            print(idx, track['artists'][0]['name'], " – ", track['name'], track['id'])
            list_of_track_id1.add(track['id'])

    return list_of_track_id1
