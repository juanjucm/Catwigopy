

class User:
    name = None
    user_name = None
    tweets = None

    def __init__(self, user_name):
        self.user_name = user_name

    def set_name(self, name):
        self.name = name

    def set_tweets(self, tweets):
        self.tweets = tweets
