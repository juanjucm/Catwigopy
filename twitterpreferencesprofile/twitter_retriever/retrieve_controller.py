# Offers an interface adapting the twitter API to project necessities.

from .tcrawler import TCrawler


# Obtains all tweets searching by one or more dictionaries. Then push them into a csv.file
def get_tweets():
    pass


# Gets a certain number tweets form a given user's timeline.
def get_user_timeline(user, number_of_tweets=all):
    pass


# Gets a certain number of user's followed users.
def get_followed_users(user, number_of_users=all):
    pass

