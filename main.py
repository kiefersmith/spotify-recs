import get, save, load, playlist, sys, pandas

pandas.set_option('display.max_columns', None)

def main():
    playlist_file = "my_playlists"
    user = "124528315"
    playlist_list = ["mist", "dead", "blavk", "classic metal"]

    g = get.Get(user)
    s = save.Save()
    l = load.Load()

#TODO add switch for what mode the user wants
    # collect all frames and lists in a class or something
    # mode switching

    # lt = g.liked_tracks()
    # lt = pandas.DataFrame(lt['items'])
    # s.csv(lt, "liked")
    #
    up = g.user_playlists()
    up = pandas.DataFrame(up['items'])
    s.csv(up, playlist_file)

    tracks_dict = {}
    recs_dict = {}
    generated_playlists = []

    df = l.csv(playlist_file)

    #getting five tracks from playlists
    for name in playlist_list:
        print(name)
        tracks_dict[name] = []
        rows = df.loc[df['name'].isin(playlist_list)]
        named = rows.loc[df['name'] == name]
        t = g.playlist_tracks(named['id'].values[0])
        t = pandas.DataFrame(t[-5:])
        for track in t['track']:
            tracks_dict[name].append(track['id'])

        s.csv(t, "playlist_tracks_" + name)

    #get recommendations and put them in a playlist or make a new one
    for name in playlist_list:
        recs_dict[name] = []
        recs_frame = pandas.DataFrame()
        recs = g.recommendations(tracks_dict[name])
        for track in recs['tracks']:
            recs_frame = recs_frame.append(track, ignore_index=True)
            recs_dict[name].append(track['id'])
        s.csv(recs_frame, "playlist_recs_" + name)

        print(recs_dict)

        p = playlist.Playlist(user, name + "_recs", False, "Auto generated recommendations for " + name + " playlist")
        vals = df[df['name'].str.match(name + "_recs")]['id'].values
        if len(vals) > 0 & len(vals) < 2:
            existing_id = vals
            print(existing_id[0])
            p.add_tracks(existing_id, recs_dict[name])
        elif len(vals) > 2:
            print("ya fucked up")
        else:
            generated = p.create()
            print(generated['id'])
            p.add_tracks(generated['id'], recs_dict[name])

if __name__ == "__main__":
     main()
