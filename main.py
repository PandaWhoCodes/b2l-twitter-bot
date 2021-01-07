import tweepy
from time import sleep
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q="#b2l_project").items():
    try:
        print("Tweet by: @" + tweet.user.screen_name)
        # perform a retweet
        tweet.retweet()
        #    possibility of it retweeting my own tweets.
        # TODO: check to see if it is retweeting its own tweets and then avoid them
        tweet.favorite()
        # Like the tweet
        # Follow the person if you're not already following
        # TODO: Add a tweepy if condition to check if im not already followiing the user
        tweet.user.follow()

    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
