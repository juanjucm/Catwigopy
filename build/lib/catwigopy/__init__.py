import catwigopy.twitter_manager as tm
from catwigopy.User import User
from catwigopy.auxiliar import *
from catwigopy.analysis import *
import pickle

name = "catwigopy"


class Catwigopy:

    # Class attribute configured via class method.
    api = None
    _user = None

    def __init__(self, user_name, consumer_key, consumer_secret, access_token, access_token_secret):
        self.api = tm.do_authentication(consumer_key, consumer_secret, access_token, access_token_secret)
        result = tm.get_user_info(self.api, user_name)
        self._user = User(user_name, result[0], result[1], result[2])

    # Retrieves user tweets
    def search_user_timeline(self, number_of_tweets):
        # Retrieve the timeline and load tweets into user
        self._user.load_tweets(tm.search_user_tweets(self.api, self._user.user_name, number_of_tweets))

    def search_user_followed(self, number_of_users):
        # Retrieve followed users
        self._user.followed_users = tm.get_user_follows(self.api, self._user.user_name, number_of_users)

    # Classify using NMF with the best hyperparameter configuration acquired in training phase.
    def classify_tweets_nmf(self):
        if self._user.analysis_results['nmf'] is None:
            # Get models pickles from folder
            with open('../data/models/nmf/nmf_29_2_01_05_nndsvda_noTermLimitTfidf.pickle', 'rb') as f:
                nmf = pickle.load(f)

            with open('../data/models/nmf/tfidf.pickle', 'rb') as f:
                tfidf = pickle.load(f)

            with open('../data/models/nmf/tfidf_vectorizer.pickle', 'rb') as f:
                tfidf_vectorizer = pickle.load(f)

            doc = " ".join(self._user.tweets['preprocessed'])
            self._user.analysis_results['nmf'] = apply_nmf(nmf, tfidf, tfidf_vectorizer, doc)

    def get_analysis_results(self):
        return self._user.analysis_results['nmf']

    def get_user_name(self):
        return self._user.name

    def get_user_username(self):
        return self._user.user_name

    def get_user_description(self):
        return self._user.description

    def get_user_image(self):
        return self._user.image
