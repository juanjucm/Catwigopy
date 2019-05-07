import catwigopy.twitter_manager as tm
from catwigopy.User import User
from catwigopy.auxiliar import *


class Catwigopy:

    # Class attribute configured via class method.
    api = None
    user = None

    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.api = tm.do_authentication(consumer_key, consumer_secret, access_token, access_token_secret)

    # Retrieves user information
    def search_user(self, user_name, number_of_tweets, number_of_users):
        # Create user
        self.user = User(user_name)

        # Retrieve the timeline and load tweets into user
        #self.user.load_tweets(tm.search_user_tweets(self.api, user_name, number_of_tweets))

        # Retrieve followed users
        self.user.followed_users = tm.get_user_follows(self.api, user_name, number_of_users)
