"""
Driver to run times
"""
import os
from datetime import datetime
from twitter_mysql import TweetAPI
from twitter_objects import Tweet

import csv
import random


def tweet_api_performance():
    # Authenticate
    api = TweetAPI(os.environ["TWITTER_USER"], os.environ["TWITTER_PASSWORD"], "twitter_db")

    start_time = datetime.now()
    # Testing tweets posted
    # read tweet csv file
    # file = 'hw1_data/tweet.csv'
    file = 'tweets_sample.csv'
    with open(file, 'r') as csvfile:
        db_tweet = csv.reader(csvfile)  # readlines
        # remove header
        next(db_tweet, None)

        # iterate through each row in tweet csv
        for row in db_tweet:
            # print(row)
            # each row extract tweet
            user_id, tweet_text = int(row[0]), row[1]
            # Register a new tweet
            t = Tweet(None, user_id, None, tweet_text)
            # call api.post tweet
            api.post_tweet(t)

        # calculates the total seconds taken and divides it by 1 million to get the tweets posted/second.
        # print("end of for loop")
        end_time = datetime.now()
        elapsed_time = (end_time - start_time).total_seconds()
        # tweets insert per second = number of tweets * 1000 / elapsed time
        tweets_per_second = 10 / elapsed_time
        print(f"post tweet calls per second: {tweets_per_second}")

        # Testing homeline
        #  Pick 30 random users, get 30 users' unique home pages, and calculate number of timelines retrieved per second.
        start_time = datetime.now()
        for i in range(1000):
            random_id = random.randint(1, 10)
            api.get_timeline(random_id)
        end_time = datetime.now()
        elapsed_time = (end_time - start_time).total_seconds()
        # calls/seconds-> current average apis per second
        timelines_per_second = 1000 / elapsed_time
        print(f"Homeline tweets per second: {timelines_per_second}")

    # api.close_connect()