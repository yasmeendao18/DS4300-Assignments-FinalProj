# Test strategy 2
import operator
import time

from twitter_redis import TweetAPI


class ExtendedTweetAPI(TweetAPI):

    def __init__(self):
        super().__init__()

    def post_tweet(self, t):
        tweet_id = self.r.incr("tweet:nextid")
        tweet_data = {
            "user_id": t.user_id,
            "tweet_text": t.tweet_text,
            "timestamp": time.time()
        }
        self.r.set(f"tweet:{tweet_id}", tweet_data)
        self.followers(tweet_id, t.user_id)

    def get_timeline(self, user_id):
        timeline = []
        following = self.r.smembers(f"following:{user_id}")
        for followee_id in following:
            followee_timeline = self.r.lrange(f"timeline:{followee_id}", 0, 9)
            for tweet_id in followee_timeline:
                tweet_content = self.r.get(f"tweet:{tweet_id}")
                if tweet_content:
                    timeline.append(tweet_content)  # Tweet(tweetID, posterID, dt, txt);
        # timeline.sort(key=operator.itemgetter("timestamp"), reverse=True)
        return timeline[:10]

    def followers(self, tweet_id, user_id):
        followers = self.r.smembers(f"followers:{user_id}")
        for follower_id in followers:
            self.r.lpush(f"timeline:{follower_id}", tweet_id)
