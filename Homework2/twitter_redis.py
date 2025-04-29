"""
Twitter Database API for Redis
"""

import redis
from datetime import datetime
import time


class TweetAPI:

    def __init__(self):
        # Create a connection and clear the database
        self.r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
        # self.flush()

    def flush(self):
        self.r.flushall()

    def post_tweet(self, t):
        # call redis function and increment by 1
        tweet_id = self.r.incr("tweet:nextid")

        # get user
        user_id = t.user_id
        # get tweet (string of text)
        tweet_text = t.tweet_text

        # convert datetime
        tweet_ts = time.time()

        # use hset(redis)
        self.r.hset(f"tweets:{t.tweet_id}",
                    mapping={"tweet_user": user_id, "tweet_text": tweet_text, "tweet_ts": tweet_ts})

        # Call the get_followers method
        self.get_followers(tweet_id, user_id)

    def get_timeline(self, user_id):

        # for  a particular user_id get timeline which is a list of tweet_id
        timeline_key = f"timeline:{user_id}"
        tweet_ids = self.r.lrange(timeline_key, 0, 9)
        timeline = []
        for tweet_id in tweet_ids:
            tweet_key = f"tweets:{tweet_id}"
            tweet_data = self.r.hgetall(tweet_key)
            if tweet_data:
                timeline.append(tweet_data)
        return timeline  # return list of tweets

    def get_followers(self, tweet_id, user_id):
        # separate followers function to improve runtime
        followers = self.r.lrange(f"followers:{user_id}", 0, -1)
        for follower in followers:
            self.r.lpush("timeline:" + follower, [str(tweet_id)])
