import spotipy

class Playlist:
    scope = 'playlist-modify-private'
    token = spotipy.util.prompt_for_user_token("kieferisgreat@gmail.com", scope)
    sp = spotipy.Spotify(auth=token)

    def __init__(self, user, name, public, description):
        self.user = user
        self.name = name
        self.public = False
        self.description = "Auto generated playlist with recommendations."

    def create(self):
        playlist = self.sp.user_playlist_create(self.user, self.name, self.public, self.description)
        return playlist

    def add_tracks(self, playlist_id, tracks):
        self.sp.user_playlist_add_tracks(self.user, playlist_id, tracks)
