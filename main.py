import get, save, load, playlist, actions, sys, pandas, spotipy

pandas.set_option('display.max_columns', None)

def main():
    user = "124528315"
    playlist_list = ["mist", "dead", "blavk", "classic metal"]

    scopes = 'playlist-read-private,playlist-modify-private'
    token = spotipy.util.prompt_for_user_token("kieferisgreat@gmail.com", scopes)
    sp = spotipy.Spotify(auth=token)

    g = get.Get(user, sp)
    s = save.Save()
    l = load.Load()
    a = actions.Actions(g, s, l, user, playlist_list, sp)

#TODO add switch for what mode the user wants
    # collect all frames and lists in a class or something
    # mode switching

    a.get_user_playlists()
    a.get_recommendations()

if __name__ == "__main__":
     main()
