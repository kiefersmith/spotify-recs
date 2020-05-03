import pandas, playlist

class Actions:
    def __init__(self, get, save, load, user, spotipy):
        self.g = get
        self.s = save
        self.l = load
        self.user = user
        self.sp = spotipy

    def get_recommendations(self, name):
        tracks_dict = {}
        features_dict = {}
        recs_dict = {}
        generated_playlists = []

        df = self.l.csv('my_playlists')

        #getting five tracks from playlists
        print(name)
        tracks_dict[name] = []
        rows = df.loc[df['name'].isin([name])]
        named = rows.loc[df['name'] == name]
        t = self.g.playlist_tracks(named['id'].values[0])
        t = pandas.DataFrame(t[-5:])
        for track in t['track']:
            tracks_dict[name].append(track['id'])

        self.s.csv(t, "playlist_tracks_" + name)

        #get audio features
        # a = self.sp.audio_features(t)
        # features_frame = pandas.DataFrame(a)
        for p in tracks_dict:
            features_dict[p] =  self.g.features_ideal(tracks_dict[p], name)

        #get recommendations and put them in a playlist or make a new one
        recs_dict[name] = []
        recs_frame = pandas.DataFrame()
        recs = self.g.recommendations(tracks_dict[name], **features_dict[name])
        for track in recs['tracks']:
            recs_frame = recs_frame.append(track, ignore_index=True)
            recs_dict[name].append(track['id'])
        self.s.csv(recs_frame, "playlist_recs_" + name)

        print(recs_dict)

        p = playlist.Playlist(self.user, self.sp, name + "_recs", False, "Auto generated recommendations for " + name + " playlist")
        vals = df[df['name'].str.match(name + "_recs")]['id'].values
        if len(vals) > 0 & len(vals) < 2:
            existing_id = vals
            print(existing_id[0])
            p.add_tracks(existing_id[0], recs_dict[name])
        elif len(vals) > 2:
            print("ya fucked up")
        else:
            generated = p.create()
            print(generated['id'])
            p.add_tracks(generated['id'], recs_dict[name])
        return

    def get_user_playlists(self):
        up = self.g.user_playlists()
        up = pandas.DataFrame(up['items'])
        self.s.csv(up, 'my_playlists')
        return

    def get_liked_tracks(self):
        lt = self.g.liked_tracks()
        lt = pandas.DataFrame(lt['items'])
        self.s.csv(lt, "liked")
