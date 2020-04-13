
class Get:
    def __init__(self, user, spotipy):
        self.user = user
        self.sp = spotipy

    def liked_tracks(self):
        liked_tracks = self.sp.current_user_saved_tracks(limit=20, offset=0)
        return liked_tracks

    def user_playlists(self):
        user_playlists = self.sp.user_playlists(self.user)
        return user_playlists

    def genre_playlists(self, category):
        category_playlists = self.sp.category_playlists(category_id=category)
        playlist_items = category_playlists['playlists']['items']
        playlists_frame = pandas.DataFrame(playlist_items)
        return playlists_frame

    def playlist_tracks(self, playlist_id):
        results = self.sp.playlist_tracks(playlist_id=playlist_id)
        playlist_tracks = results['items']
        while results['next']:
            results = self.sp.next(results)
            playlist_tracks.extend(results['items'])
        return playlist_tracks

    def recommendations(self, seed_tracks):
        recs = self.sp.recommendations(seed_tracks=seed_tracks[-5:])
        return recs
