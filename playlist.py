
class Playlist:
    def __init__(self, user, spotipy, name, public, description):
        self.user = user
        self.sp = spotipy
        self.name = name
        self.public = False
        self.description = "Auto generated playlist with recommendations."

    def create(self):
        playlist = self.sp.user_playlist_create(self.user, self.name, self.public, self.description)
        return playlist

    def add_tracks(self, playlist_id, tracks):
        self.sp.user_playlist_add_tracks(self.user, playlist_id, tracks)
