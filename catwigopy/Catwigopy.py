
import catwigopy.twitter_manager as tm
from catwigopy.User import User
from catwigopy.auxiliar import *

class Catwigopy:

    # Class attribute configured via class method.
    __api = None
    user = None

    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        Catwigopy.authenticate(consumer_key, consumer_secret, access_token, access_token_secret)


    @classmethod
    def authenticate(cls, consumer_key, consumer_secret, access_token, access_token_secret):
        if cls.__api is None:
            cls.__api = tm.do_authentication(consumer_key, consumer_secret, access_token, access_token_secret)

    # Analyse user tweets with the main
    def analyse_user_tweets(self, user_name):
        # Create user
        self.user = User(user_name)

        # Retrieve the timeline
        self.user.load_tweets(tm.search_user_tweets(self.__api, user_name, 2000))

        # Preprocess Tweets
        preprocess_tweets(self.user.tweets['text'])

