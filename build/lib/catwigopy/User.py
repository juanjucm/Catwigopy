import pandas as pd
import numpy as np
import threading
from multiprocessing import Pool
from catwigopy.auxiliar import *
from catwigopy.twitter_manager import *


class User:
    name = None
    user_name = None
    image = None
    description = None
    tweets = None
    followed_users = None
    analysis_results = None

    def __init__(self, user_name, image_url, name, description):
        self.user_name = user_name
        self.image = image_url
        self.name = name
        self.description = description
        self.analysis_results = {'nmf': None, 'kmeans': None}

    def load_tweets(self, tweets):
        self.tweets = pd.DataFrame(tweets)
        self.tweets['preprocessed'] = None

        # Preprocess the tweets dividing the task in 4 threads.
        arrays_to_preprocess = np.array_split(self.tweets, 5)

        pool = Pool(processes=5)
        mp_answer = pool.map_async(self.preprocessing_handler, (array for array in arrays_to_preprocess))

        self.tweets = pd.concat(mp_answer.get())

    def preprocessing_handler(self, df_to_preprocess):
        for index, row in df_to_preprocess.iterrows():
            row['preprocessed'] = preprocess_tweet(row['text'])
        return df_to_preprocess
