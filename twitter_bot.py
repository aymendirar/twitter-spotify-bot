import tweepy
import time
import spotify_client

from secrets import twitter_api_key, twitter_api_secret_key, twitter_access_token, twitter_access_token_secret

FILE_NAME = 'last_seen_id.txt'

# sets up bot for use in file
auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret_key)
auth.set_access_token(twitter_access_token, twitter_access_token_secret)
twitter_api = tweepy.API(auth)
        
# EFFECTS: gets the last seen id that was tweeted at the bot
def get_last_seen_id():
    f_read = open(FILE_NAME, "r")
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

# EFFECTS: writes the new last seen id to the last_seen_id file
def store_last_seen_id(last_seen_id):
    f_write = open(FILE_NAME, "w")
    f_write.write(str(last_seen_id))
    f_write.close()
    return
        
# EFFECTS: gets most recent replies, calls spotify client to make a playlist, replies back to user when done
def run_twitter_bot():
    try: 
        last_seen_id = get_last_seen_id()
        print(last_seen_id)
    except:
        last_seen_id = 1267983029684690944 # place holder if last_seen_id is empty
    
    mentions = twitter_api.mentions_timeline(last_seen_id)
    
    for mention in reversed(mentions):
        tweet_content = mention.text
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id)
        
        print(tweet_content)
        list_of_tweet_words = tweet_content.split(" ")
        
        # if the tweet was formatted correctly
        if len(list_of_tweet_words) == 3:
            spotify_username = list_of_tweet_words[1]
            search_string = list_of_tweet_words[2]
            try: 
                spotify_bot = spotify_client.SpotifyClient(spotify_username)
                spotify_bot.create_playlist_with_tracks(search_string)
                playlist_url = spotify_bot.playlist_url
                twitter_api.update_status("@" + mention.user.screen_name + " Your new playlist was created! Click this link to listen to check it out: " + playlist_url, mention.id)
            except:
                twitter_api.update_status("@" + mention.user.screen_name + " Hey! Something went wrong when I tried connecting to Spotify. Please make sure your username is correct and try again. If the problem persists, please contact the developer.", mention.id)
        else:
            twitter_api.update_status("@" + mention.user.screen_name + " Hey! It looks like you didn't format the playlist request in a way I can I understand :(. Please check my account bio and try again!", mention.id)

# runs the bot every 15 seconds
while True:
    run_twitter_bot()
    time.sleep(15)
