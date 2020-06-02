import tweepy
import time

from secrets import twitter_api_key, twitter_api_secret_key, twitter_access_token, twitter_access_token_secret

class TwitterClient:
    # EFFECTS: sets up client for use
    def __init__(self):
        auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret_key)
        auth.set_access_token(twitter_access_token, twitter_access_token_secret)
        self.twitter_api = tweepy.API(auth)
        self.FILE_NAME = 'last_seen_id.txt'
        self.last_seen_id = None    
        
    # EFFECTS: gets mentions 
    def get_mentions(self):
        mentions = self.twitter_api.mentions_timeline(self.last_seen_id, tweet_mode ="extentded")
        
        for mention in reversed(mentions):
            tweet_content = mention.text
            print(tweet_content)
            type(tweet_content)
            print(tweet_content.split(" "))
            
    # EFFECTS: gets the last seen id that was tweeted at the bot
    def get_last_seen_id(self):
        f_read = open(self.FILE_NAME, "r")
        last_seen_id = int(f_read.read().strip())
        f_read.close()
        return last_seen_id
    
    # EFFECTS: writes the new last seen id to the last_seen_id file
    def store_last_seen_id(self):
        f_write = open(self.FILE_NAME, "w")
        f_write.write(str(self.last_seen_id))
        f_write.close()
        return
    
    def reply_back(self, playlist_link):
        pass
        # send out tweet with @ saying here's your link
        
bot = TwitterClient()
bot.get_mentions()
