"""
Tweet Class
"""
class Tweet:

    def __init__(self, tweet_id, user_id, tweet_ts, tweet_text):
        self.tweet_id = tweet_id
        self.user_id = user_id
        self.tweet_ts = tweet_ts
        self.tweet_text = tweet_text

    def __str__(self):
        return f"Tweet: {self.tweet_id} {self.user_id} {self.tweet_ts}({self.tweet_text})"

