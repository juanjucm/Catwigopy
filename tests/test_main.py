#Perform main tests

import time

from catwigopy import Catwigopy

consumer_key, consumer_secret, access_token, access_token_secret = ["WGH1yjqPiQg92igLjnhCg1wlC", "UwlSBz5Xxk7gConanvjq3XLOyHoCfVZk6JPSF7XOZMJvDu9NN4", "254490342-urFr0JJqjpHxYEvfg1JC2a2DtnHGIrD1lFqxSiOU", "EkxTbenoDae8cmDepAPJkDQ0WLyna6gNc4drmx07KWieh"]

cat = Catwigopy('Disney', consumer_key, consumer_secret, access_token, access_token_secret)

start1 = time.time()
cat.get_topics_top_terms()
end1 = time.time()
print(end1 - start1)

start2 = time.time()
cat.get_topics_top_terms()
end2 = time.time()
print(end2 -start2)