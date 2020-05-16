# Simple Spotify Recommendation Generator

A few scripts that use recently liked Spotify tracks to generate recommendations.

## Usage

Export `SPOTIPY_CLIENT_ID`, `SPOTIPY_CLIENT_SECRET`, `SPOTIPY_REDIRECT_URI`. (I do this in a shell script before use.)

Then you can run the script.  Playlist names should be in quotes, separated from one another by spaces.

`python3 main.py <your_user_id> <playlist_name> ...`
