import catwigopy.twitter_manager as tm
from catwigopy.User import User
from catwigopy.auxiliar import *
from catwigopy.analysis import *
import pandas as pd
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

    # Retrieves user tweets and preprocess them
    def search_user_timeline(self, number_of_tweets=1200):
        # Retrieve the timeline, preprocess the tweets and load them as dataFrame
        self._user.tweets = pd.DataFrame(tm.search_user_tweets(self.api, self._user.user_name, number_of_tweets))

    # Classify using NMF with the best hyperparameter configuration acquired in training phase.
    def get_user_classification(self):
        if self._user.analysis_results['nmf'] is None:
            # Get models pickles from folder
            with open('../data/models/nmf/nmf_29_2_01_05_nndsvda_noTermLimitTfidf.pickle', 'rb') as f:
                nmf = pickle.load(f)

            with open('../data/models/nmf/tfidf.pickle', 'rb') as f:
                tfidf = pickle.load(f)

            with open('../data/models/nmf/tfidf_vectorizer.pickle', 'rb') as f:
                tfidf_vectorizer = pickle.load(f)

            doc = " ".join(self._user.tweets['preprocessed_tweet'])
            self._user.analysis_results['nmf'] = apply_nmf(nmf, tfidf, tfidf_vectorizer, doc)

        return self._user.analysis_results['nmf']

    def get_user_name(self):
        return self._user.name

    def get_user_username(self):
        return self._user.user_name

    def get_user_description(self):
        return self._user.description

    def get_user_image(self):
        return self._user.image

    # Returns a list of dictionaries with shape {text: #hashtag, count: 12}
    def get_hashtags_terms_count(self):
        return generate_occurences_dictionay([l for l in self._user.tweets['hashtags'] if l])

    # Returns a list of dictionaries with shape {text: term, count: 12}
    def get_tweet_terms_count(self):
        return generate_occurences_dictionay([l for l in self._user.tweets['preprocessed_tokens'] if l])

