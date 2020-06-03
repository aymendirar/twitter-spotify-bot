# Twitter Spotify Playlist Generator

This is a Twitter bot that, when tweeted at with a username and an artist name, will make a Spotify playlist of that artist's top tracks. The Twitter bot will then reply back to users with the link for their new playlist.  

## How to use:

In order for it work properly the tweet should be formatted as the following:
> @spotify_gen [username] [search-string]

where the _username_ is your spotify username obtained by heading over to [accounts.spotify.com](https://accounts.spotify.com/), signing in, and looking at your "Account overview" tab. The _search-string_ should be a single word artist name. As of now, there is no support for multi-word artist names, but usually, picking the most significant word in a multi-word artist name tends to do the trick. Feel free to fork this repo and add that functionality if you'd like!

## Screenshots

### Twitter bot interaction:

<img src = "screenshots/img_1.png" width = 400>

### The created playlist:

<img src = "screenshots/img_2.png" width = 400>
