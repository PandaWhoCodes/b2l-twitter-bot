import tweepy
import schedule
import time
from time import sleep
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def run_tasks():
    with open("user_list.txt") as f:
        users = f.readlines()
# TODO: Use different words randomly instead of just one static query
    for user in users:
        tweet = "Hello @"+user+" How's it going with your #b2l_project?"
        api.update_status(status=tweet)
# TODO: change it to one a week
    schedule.every(30).minutes.do(run_tasks)
    while True:
        schedule.run_pending()
        time.sleep(1)
    return
# TODO: Add emojis / images / gifs to the responses

if __name__ == "__main__":
    run_tasks()