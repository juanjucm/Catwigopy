import pandas as pd
import numpy as np
import threading
from multiprocessing import Pool
from catwigopy.auxiliar import *
from catwigopy.twitter_manager import *


class User:

    """
    class representing the user
    """

    name = None
    user_name = None
    image = None
    description = None
    tweets = None
    analysis_results = None
    tweets_terms = None
    hashtags_terms = None

    def __init__(self, user_name, image_url, name, description, tweets):
        self.user_name = user_name
        self.image = image_url
        self.name = name
        self.description = description
        self.tweets = tweets
        self.analysis_results = {'nmf': None, 'kmeans': None}
