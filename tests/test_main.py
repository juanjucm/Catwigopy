#Perform main tests

from catwigopy import Catwigopy

consumer_key, consumer_secret, access_token, access_token_secret = ["Q2OBHvyHL0jPUGfKpg2JvYO4O", "nR6rG8RaFxpQMQvrMUX6twhZCf6UNp4wx8MiV5okV53qgSwOp7", "993175870545293312-GvTQWOBF07UUKJFLPhy2l0wptkZDuA0", "mQ3bII85nPUjtP0FWHbR8t34ft22KY3wGtACqKfTaRuyk"]

cat = Catwigopy(consumer_key, consumer_secret, access_token, access_token_secret)

cat.search_user('Tesla', 1200, 10000)

print(cat.user.followed_users)


