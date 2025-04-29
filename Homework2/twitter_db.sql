CREATE DATABASE twitter_db;
USE twitter_db;

SET GLOBAL local_infile=ON;

CREATE TABLE TWEET (
	tweet_id INT PRIMARY KEY auto_increment,
    user_id INT UNIQUE,
    tweet_ts DATETIME,
    tweet_text VARCHAR(140)
); 

CREATE TABLE FOLLOWS (
    user_id INT,
    follows_id INT,
    PRIMARY KEY (user_id, follows_id)
);

LOAD DATA LOCAL INFILE 'C:\Users\yazzy\DS4300\Homework1\hw1_data\follows.csv'
INTO TABLE FOLLOWS;




