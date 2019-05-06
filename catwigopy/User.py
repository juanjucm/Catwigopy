import pandas as pd


class User:
    name = None
    user_name = None
    tweets = None

    def __init__(self, user_name):
        self.user_name = user_name

    def load_tweets(self, tweets):
        self.tweets = pd.DataFrame(tweets)

    def set_name(self, name):
        self.name = name
