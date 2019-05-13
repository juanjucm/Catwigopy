import tweepy
from pprint import pprint


def do_authentication(consumer_key, consumer_secret, access_token, access_token_secret):
    # Authentication process:
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth,
                     # check remaining calls and block until replenished
                     wait_on_rate_limit=True,
                     # retry 3 times with 5 seconds delay when getting these error codes
                     retry_count=3,
                     retry_delay=5,
                     retry_errors=set([401, 404, 500, 503]))

    return api


def search_user_tweets(api, user_screen_name, number_of_tweets):
    tweets_array = list()

    tweets = [tweet._json for tweet in tweepy.Cursor(api.user_timeline, id=user_screen_name, tweet_mode='extended').items(number_of_tweets) if not 'retweeted_status' in tweet._json.keys()]

    for tweet in tweets:
        # Get the text and hashtags
        text = tweet['full_text']
        hashtags = [h['text'] for h in tweet['entities']['hashtags']]

        # Create the document
        twt = {'text': text,
               'hashtags': hashtags,
               }

        tweets_array.append(twt)

    return tweets_array


def get_user_follows(api, user_screen_name, number_of_users):
    followed_users = [user.screen_name for user in tweepy.Cursor(api.friends, screen_name=user_screen_name).items(number_of_users)]
    return followed_users


# Returns user image, name and description
def get_user_info(api, user_screen_name):
    tweet = [tweet._json for tweet in tweepy.Cursor(api.user_timeline, id=user_screen_name, tweet_mode='extended').items(1)][0]
    return tweet['user']['profile_image_url_https'], tweet['user']['name'], tweet['user']['description']

