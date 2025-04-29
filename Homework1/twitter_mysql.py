"""
Twitter Database API for MySQL
"""
from dbutils import DBUtils
from twitter_objects import Tweet


class TweetAPI:

    def __init__(self, user, password, database, host="localhost"):
        self.dbu = DBUtils(user, password, database, host)

    def post_tweet(self, t):
        sql = "INSERT INTO tweet (tweet_ts, tweet_text) VALUES (%s, %s)"
        val = (t.tweet_ts, t.tweet_text)
        self.dbu.insert_one(sql, val)
        # print("testing post_tweet")

    def get_timeline(self, user_id):
        sql = """
        SELECT T.* FROM TWEET AS T 
        JOIN FOLLOWS AS F ON T.USER_ID = F.FOLLOWS_ID 
        WHERE F.USER_ID = %s
        ORDER BY T.TWEET_TS DESC LIMIT 10
        """
        val = (user_id,)
        df = self.dbu.execute(sql,val)
        # tweets = [Tweet(*df.iloc[i][1:]) for i in range(len(df))]
        tweets = [Tweet(tweet_id=df.iloc[i]['tweet_id'],
                        user_id=df.iloc[i]['user_id'],
                        tweet_ts=df.iloc[i]['tweet_ts'],
                        tweet_text=df.iloc[i]['tweet_text']) for i in range(len(df))]
        return tweets

    def get_followers(self, user_id):
        sql = "SELECT user_id FROM FOLLOWS WHERE follows_id = %s"
        # val = (user_id)
        df = self.dbu.execute(sql)
        followers = df['user_id'].toList()
        return followers

    def get_followees(self, user_id):
        sql = "SELECT follows_id FROM FOLLOWS WHERE user_id = %s"
        val = (user_id,)
        df = self.dbu.execute(sql, val)
        followers = df['follows_id'].toList()
        return followers

    def get_tweets(self, user_id):
        sql = "SELECT * FROM TWEET WHERE user_id = %s ORDER BY tweet_ts"
        # val = (user_id)
        df = self.dbu.execute(sql)
        tweets = [Tweet(*df.iloc[i][1:]) for i in range(len(df))]
        return tweets



