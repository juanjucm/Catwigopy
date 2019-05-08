import catwigopy.twitter_manager as tm
from catwigopy.User import User
from catwigopy.auxiliar import *
from catwigopy.analysis import *
import pickle


class Catwigopy:

    # Class attribute configured via class method.
    api = None
    user = None

    def __init__(self, user_name, consumer_key, consumer_secret, access_token, access_token_secret):
        self.api = tm.do_authentication(consumer_key, consumer_secret, access_token, access_token_secret)
        self.user = User(user_name)

    # Retrieves initial user information
    def search_user(self, number_of_tweets, number_of_users):
        # Retrieve the timeline and load tweets into user
        self.user.load_tweets(tm.search_user_tweets(self.api, self.user.user_name, number_of_tweets))

        # Retrieve followed users
        self.user.followed_users = tm.get_user_follows(self.api, self.user.user_name, number_of_users)

    # Classify using NMF with the best hyperparameter configuration acquired in training phase.
    def classify_tweets_nmf(self):
        if self.user.analysis_results['nmf'] is None:
            # Get models pickles from folder
            with open('../data/models/nmf/nmf_80_2_01_05_nndsvda_noTermLimitTfidf.pickle', 'rb') as f:
                nmf = pickle.load(f)

            with open('../data/models/nmf/tfidf.pickle', 'rb') as f:
                tfidf = pickle.load(f)

            with open('../data/models/nmf/tfidf_vectorizer.pickle', 'rb') as f:
                tfidf_vectorizer = pickle.load(f)

            doc = " ".join(self.user.tweets['preprocessed'])
            self.user.analysis_results['nmf'] = apply_nmf(nmf, tfidf, tfidf_vectorizer, doc)

    def get_analysis_results(self):
        return self.user.analysis_results['nmf']