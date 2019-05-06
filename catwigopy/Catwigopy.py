
import catwigopy.twitter_manager as tm
from catwigopy.User import User

class Catwigopy:

    # Class attribute configured via class method.
    __api = None
    users = None

    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.users = list()
        Catwigopy.authenticate(consumer_key, consumer_secret, access_token, access_token_secret)


    @classmethod
    def authenticate(cls, consumer_key, consumer_secret, access_token, access_token_secret):
        if cls.__api is None:
            cls.__api = tm.do_authentication(consumer_key, consumer_secret, access_token, access_token_secret)

    def analyse_user(self, user_name):
        user = User(user_name)
        self.users.append(user)

        user.set_tweets(tm.search_user_tweets(self.__api, user_name, 2000))

