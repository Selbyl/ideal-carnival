import tweepy
import time
import csv
while True:
    time.sleep(10)
    client = tweepy.Client(bearer_token='Bearer Token')
    api = tweepy.API(client, wait_on_rate_limit=True, timeout=60, retry_count=10, retry_delay=30)

    # Replace with your own search query
    query = 'cybersecurity, hack, ransomware -is:retweet has:media'

    tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'],
                                     media_fields=['preview_image_url'], expansions='attachments.media_keys',
                                     max_results=100)

# Get list of media from the includes object
    media = {m["media_key"]: m for m in tweets.includes['media']}

    for tweet in tweets.data:
        attachments = tweet.data['attachments']
        media_keys = attachments['media_keys']
        #tweet_fields = 'contaxt_annotations'
        print(tweet.text)
        if media[media_keys[0]].preview_image_url:
             print(media[media_keys[0]].preview_image_url)
