import tweepy

from secrets import twitter_api_key, twitter_api_secret_key, twitter_access_token, twitter_access_token_secret

class TwitterClient:
    def __init__(self):
        auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret_key)
        auth.set_access_token(twitter_access_token, twitter_access_token_secret)
        api = tweepy.API(auth)