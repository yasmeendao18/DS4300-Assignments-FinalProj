"""
filename: dbutils.py

description: A collection of database utilities to make it easier
to implement a database application
"""

import mysql.connector
import pandas as pd
import redis


class DBUtils:

    def __init__(self, host="localhost", port=6379, db=0):
        """ Initialize Redis connection """
        self.r = redis.Redis(host=host, port=port, db=db)
