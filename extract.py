import tweepy
import pandas as pd
import json
import os
from datetime import datetime




def twitter_etl():
   #load the environment variables
    access_key = "1049560705098235904-nfeoIT9JkvUSncbmN3TQztV1qvwzgN"
    access_secret = "Xs7y2Gag6qXKM048Q4kgg4fhxg0loDAgop53hfXbybnB2"
    consumer_key = "SXa0IeyVRoxVZbseVglZS28YB"
    consumer_secret = "XjOn2ShPYYvN0Tjz5Cwjl9VpRxDrsutUfnjzaIQIkWNHPRLe2s"

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

    csv_filename = "tweets.csv"
    df = pd.DataFrame(tweet_list)

    df['created_at'] = pd.to_datetime(df['created_at'])


    #df.to_csv(csv_filename,index=False)
    df.to_csv("s3://tweets-datalake/python/tweetscsv/tweets.csv")