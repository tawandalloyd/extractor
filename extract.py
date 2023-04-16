import tweepy
import pandas as pd
import json
import os
from datetime import datetime
import s3fs
from dotenv import load_dotenv

#load the environment variables
load_dotenv()

# Access Twitter API credentials from environment variables
access_key = os.getenv('TWITTER_ACCESS_KEY')
access_secret = os.getenv('TWITTER_ACCESS_SECRET')
consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')


#twitter authentication
auth =  tweepy.OAuthHandler(access_key, access_secret)
auth.set_access_token(consumer_key,consumer_secret)

#creating an API object
api = tweepy.API(auth)

tweets = api.user_timeline(screen_name='@CharukaTawanda',
                           #200 is the maximum count allowed
                           count = 200,
                           include_rts = False,
                           #neccessary to keep full text
                           tweet_mode = 'extended'
                           )

tweet_list = []
for tweet in tweets:
    text= tweet._json["full_text"]
    refined_tweet = {"user": tweet.user.screen_name,
                     'text': text,
                     'favorite_count': tweet.favorite_count,
                     'retweet_count' : tweet.retweet_count,
                     'created_at' : tweet.created_at
                    }
    tweet_list.append(refined_tweet)

df = pd.DataFrame(tweet_list)
df.to_csv("mytweets.csv")