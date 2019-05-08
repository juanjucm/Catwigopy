import pandas as pd
import numpy as np
import threading
import multiprocessing as mp
from catwigopy.auxiliar import *


class User:
    name = None
    user_name = None
    tweets = None
    followed_users = None
    analysis_results = None

    def __init__(self, user_name):
        self.user_name = user_name
        self.analysis_results = {'nmf': None, 'kmeans': None}

    def load_tweets(self, tweets):
        self.tweets = pd.DataFrame(tweets)
        self.tweets['preprocessed'] = None

        for index, row in self.tweets.iterrows():
            row['preprocessed'] = preprocess_tweet(row['text'])

        # print(self.tweets.shape)
        #
        # # Preprocess the tweets dividing the task in 4 threads.
        # arrays_to_preprocess = np.array_split(self.tweets, 4)
        #
        # output = mp.Queue()
        # processes = [mp.Process(target=self.preprocessing_handler, args=(pos, a, output)) for pos, a in enumerate(arrays_to_preprocess)]
        #
        # for p in processes:
        #     p.start()
        #
        # for p in processes:
        #     p.join()
        #
        # # Merge the results in the main dataframe
        # results = [output.get() for p in processes]
        # results.sort()
        #
        # self.tweets = pd.concat([r[1] for r in results])
        # print(self.tweets.shape)

    # def preprocessing_handler(self, pos, df_to_preprocess, output):
    #     for index, row in df_to_preprocess.iterrows():
    #         row['preprocessed'] = preprocess_tweet(row['text'])
    #
    #     output.put((pos, df_to_preprocess))