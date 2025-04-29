"""
Driver to run times
"""
from datetime import datetime
from twitter_redis import TweetAPI
from twitter_objects import Tweet
import csv
import random


def tweet_api_performance():
    # Authenticate
    tweet_api = TweetAPI()
    start_time = datetime.now()
    # Testing tweets posted
    # read tweet csv file
    # file = 'tweets_sample.csv'
    file = 'hw1_data/tweet.csv'
    with open(file, 'r') as csvfile:
        db_tweet = csv.reader(csvfile)  # readlines
        # remove header
        next(db_tweet, None)

        # iterate through each row in tweet csv
        counter = 0
        for row in db_tweet:
            # testing
            counter += 1
            print("row:", counter)
            # each row extract tweet
            user_id, tweet_text = int(row[0]), row[1]
            # Register a new tweet
            t = Tweet(None, user_id, None, tweet_text)
            # call api.post tweet
            tweet_api.post_tweet(t)

        # calculates the total seconds taken and divides it by 1 million to get the tweets posted/second.
        # print("end of for loop")
        end_time = datetime.now()
        elapsed_time = (end_time - start_time).total_seconds()
        # tweets insert per second = number of tweets * 1000 / elapsed time
        tweets_per_second = 1000000 / elapsed_time
        print(f"post tweet calls per second: {tweets_per_second}")
        # print(elapsed_time)

        # Testing home timeline Pick 30 random users, get 30 users' unique home pages, and calculate number of
        # timelines retrieved per second.
        start_time = datetime.now()
        for i in range(1000):
            random_id = random.randint(1, 10)
            tweet_api.get_timeline(random_id)
        end_time = datetime.now()
        elapsed_time = (end_time - start_time).total_seconds()
        # calls/seconds-> current average apis per second
        timelines_per_second = 1000 / elapsed_time
        print(f"Timelines per second: {timelines_per_second}")

    tweet_api.r.close()
