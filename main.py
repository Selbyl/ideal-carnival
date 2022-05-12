import tweepy
from tweepy.auth import OAuthHandler
import time
consumer_key="consumer_key"
consumer_secret="consumer_secret"
access_token="access_token"
access_token_secret="access_token_secret"

auth = tweepy.OAuthHandler(consumer_key,
                           consumer_secret)
auth.set_access_token(access_token,
                       access_token_secret)
while True:
    api = tweepy.API(auth, wait_on_rate_limit=True)  # set wait_on_rate_limit =True; as twitter may block you from querying if it finds you exceeding some limits

    search_words = ["cybersecurity"]

    date_since = "2020-05-21"

    tweets = tweepy.Cursor(api.search_tweets, search_words,
                                     #geocode = "20.5937,78.9629,3000km",
                                               lang = "en", since=date_since).items(100)
## the geocode is for India; format for geocode="lattitude,longitude,radius"
## radius should be in miles or km


    for tweet in tweets:
        print("created_at: {}\nuser: {}\ntweet text: {}\ngeo_location: {}".
            format(tweet.created_at, tweet.user.screen_name, tweet.text, tweet.user.location))
        print("\n")
## tweet.user.location will give you the general location of the user and not the particular location for the tweet itself, as it turns out, most of the users do not share the exact location of the tweet

sleep.time(10)
