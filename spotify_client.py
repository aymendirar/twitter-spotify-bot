import spotipy
from spotipy import util
from secrets import spotify_client_id, spotify_client_secret

class SpotifyClient:
    
    # EFFECTS: sets up client for use
    def __init__(self, username):
        scope = "playlist-modify-public ugc-image-upload"
        redirect_uri = "http://google.com/" # necessary redirect using spotify api and spotipy
        self.user = username
        self.token = util.prompt_for_user_token(self.user, scope, spotify_client_id, spotify_client_secret, redirect_uri)
        self.spotifyObject = spotipy.Spotify(auth=self.token)
        
    # EFFECTS: searches for songs with passed in word and creates a 10-song playlist. returns playlist link.
    def create_playlist_with_tracks(self, search_string):
        # creates a new public playlist to add songs to
        self.spotifyObject.user_playlist_create(self.user, name = "Twitter Spotify Playlist Generator's Playlist", public = True, description = "A playlist created by the twitter bot @spotify_gen")
        
        # get the playlist id and url of the playlist that was just created
        playlists = self.spotifyObject.current_user_playlists(limit = 1, offset = 0)
        playlist_id = playlists["items"][0]["id"]
        self.playlist_url = playlists["items"][0]["external_urls"]["spotify"]
        
        # get the uris of the songs obtained by searching the inputted word
        list_track_uris = self.get_tracks(search_string)
        
        # adds tracks to created playlist
        self.spotifyObject.user_playlist_add_tracks(self.user, playlist_id, list_track_uris)

    # EFFECTS: searches spotify for given artist and returns a list of their top tracks uris    
    def get_tracks(self, search_string):
        limit = 1
        
        # search spotify for given artist
        artist = self.spotifyObject.search(search_string, limit, offset = 0, type = "artist")
        
        # gets artist's uri
        artist_uri = artist["artists"]["items"][0]["uri"]
        
        # gets artsit's top songs data
        track_data = self.spotifyObject.artist_top_tracks(artist_uri)
        
        # extracts artist's top songs uris
        list_track_uris = [track_data["tracks"][i]["uri"] for i, data in enumerate(track_data["tracks"])]
        return list_track_uris
    