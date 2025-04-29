"""
Yasmeen Dao
Homework1 Twitter Relational Database with python
"""
import csv
import os
import random
from datetime import datetime

from driver import tweet_api_performance
from twitter_mysql import TweetAPI
from twitter_objects import Tweet


def main():
    # tester checks functions
    tweet_api_performance()


if __name__ == '__main__':
    main()
