# Performs Twitter retrieving tasks
# Authentication done with credentials specified in secret.py
import tweepy

# Set here your Twitter application credentials:
consumer_key = 'Q2OBHvyHL0jPUGfKpg2JvYO4O'
consumer_secret = 'nR6rG8RaFxpQMQvrMUX6twhZCf6UNp4wx8MiV5okV53qgSwOp7'
access_token = '993175870545293312-GvTQWOBF07UUKJFLPhy2l0wptkZDuA0'
access_token_secret = 'mQ3bII85nPUjtP0FWHbR8t34ft22KY3wGtACqKfTaRuyk'


class TCrawler:
    # Class attributes configured via class method.
    __api = None
    __auth = None

    def __init__(self):
        TCrawler.__do_authentication()

    @classmethod
    def __do_authentication(cls):
        if cls.__auth is None:
            # Authentication process:
            cls.__auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            cls.__auth.set_access_token(access_token, access_token_secret)

        if cls.__api is None:
            cls.__api = tweepy.API(cls.__auth,
                                   # check remaining calls and block until replenished
                                   wait_on_rate_limit=True,
                                   # retry 3 times with 5 seconds delay when getting these error codes
                                   retry_count=3,
                                   retry_delay=5,
                                   retry_errors=set([401, 404, 500, 503]))

    def search_tweets(self, query, lang, number):
        res = [status for status in
               tweepy.Cursor(self.__api.search, q=query, count=100, tweet_mode='extended', lang=lang).items(number)]

        return res

    def serach_user_tweets(self, user, lang, number):
        pass
