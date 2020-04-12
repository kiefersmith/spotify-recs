import spotipy, json, pandas, sys
import matplotlib.pyplot as plt
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
sp.trace = False

playlist_category = sys.argv[1:][0]

category_playlists = sp.category_playlists(category_id=playlist_category)
playlist_items = category_playlists['playlists']['items']
playlists_frame = pandas.DataFrame(playlist_items)

features_frame = pandas.DataFrame()
tracks_frame = pandas.DataFrame()

print("> requesting tracks / creating dataframes")
for index, row in playlists_frame.iterrows():
    print(row.name)
    results = sp.playlist(playlist_id=row.id)
    items = results['tracks']['items']

    track_ids = []
    track_data = []

    for t in items:
        try:
            track_ids.append(t['track']['id'])
        except Exception as e:
            print('ah fuck, ', e)
            pass
        # This is slow as fuck
        try:
            tracks = sp.track(track_id=t['track']['id'])
            track_data.append(tracks)
        except Exception as e:
            print('ah fuck, ', e)
            pass

    track_features = sp.audio_features(tracks=track_ids)

    tracks_frame = tracks_frame.append(track_data, ignore_index=True)
    features_frame = features_frame.append(track_features, ignore_index=True)

all_tracks = pandas.concat([features_frame, tracks_frame], axis=1, ignore_index=True)
all_tracks.columns = list(features_frame.columns.values) + list(tracks_frame.columns.values)
print("> writing files... ")
all_tracks.to_pickle(path="./data/all_tracks_"+playlist_category+".zip", compression="zip")
all_tracks.to_csv(path_or_buf="./data/all_tracks_"+playlist_category+".csv")


#all_tracks.plot.scatter(x='tempo', y='danceability')
#plt.show()

#print(all_tracks.sort_values(by='valence', ascending=True))
#sp.recommendations()

