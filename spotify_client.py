import os
import sys
import json
import webbrowser
import spotipy
from spotipy import util
from secrets import spotify_client_id, spotify_client_secret, spotify_username

class SpotifyClient:
    
    # EFFECTS: sets up client for use
    def __init__(self, username = spotify_username):
        scope = "playlist-modify-public"
        redirect_uri = "http://google.com/"
        self.user = username
        self.token = util.prompt_for_user_token(self.user, scope, spotify_client_id, spotify_client_secret, redirect_uri)
        self.spotifyObject = spotipy.Spotify(auth=self.token)
        
    # EFFECTS: searches for songs with passed in word and creates a 10-song playlist. returns playlist link.
    def create_playlist_with_tracks(self, word):
        # creates a new public playlist to add songs to
        self.spotifyObject.user_playlist_create(self.user, name = "2Twitter Spotify Playlist Generator's Playlist", public = True, description = "A playlist created by the twitter bot @spotify_gen")
        
        # get the playlist id and url of the playlist that was just created
        playlists = self.spotifyObject.current_user_playlists(limit = 1, offset = 0)
        playlist_id = playlists["items"][0]["id"]
        self.playlist_url = playlists["items"][0]["external_urls"]["spotify"]
        print(playlist_id) # the id of the playlist created by client
        print(playlist_url)
        
        # get the uris of the songs obtained by searching the inputted word
        list_track_uris = self.get_tracks(word)
        
        #adds tracks to created playlist
        self.spotifyObject.user_playlist_add_tracks(self.user, playlist_id, list_track_uris)

        
    def get_tracks(self, search_string):
        limit = 10
        
        #search spotify for songs containing the inputted search_string
        tracks = self.spotifyObject.search(search_string, limit, offset = 0, type = "track")
        
        #extracts the uris from the search
        list_track_uris = [tracks["tracks"]["items"][i]["uri"] for i in range(limit)]
        return list_track_uris
    

client = SpotifyClient()
print("worked")
client.create_playlist_with_tracks("happy")
