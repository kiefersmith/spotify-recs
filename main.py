import get, save, load, playlist, actions, sys, pandas, spotipy

pandas.set_option('display.max_columns', None)

def main():
    user = sys.argv[1]
    playlist_list = list(sys.argv[2:])
    print(sys.argv[2])

    scopes = 'playlist-read-private,playlist-modify-private'
    token = spotipy.util.prompt_for_user_token("kieferisgreat@gmail.com", scopes)
    sp = spotipy.Spotify(auth=token)

    g = get.Get(user, sp)
    s = save.Save()
    l = load.Load()
    a = actions.Actions(g, s, l, user, sp)

#TODO add switch for what mode the user wants
    # collect all frames and lists in a class or something
    # mode switching

    a.get_user_playlists()
    for name in playlist_list:
        a.get_recommendations(name)

if __name__ == "__main__":
     main()
