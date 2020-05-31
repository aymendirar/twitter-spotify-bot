import os
import sys
import json
import webbrowser
import spotipy
from spotipy import util
from secrets import spotify_client_id, spotify_client_secret, spotify_username

class SpotifyClient:
    def __init__(self):
        scope = "playlist-modify-private"
        redirect_uri = "http://google.com/"
        self.token = util.prompt_for_user_token(spotify_username, scope, spotify_client_id, spotify_client_secret, redirect_uri)
        spotifyObject = spotipy.Spotify(auth=self.token)
        
try:
    client = SpotifyClient()
    print("worked")
except:
    print("error occurred")