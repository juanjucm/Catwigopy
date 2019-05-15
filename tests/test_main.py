#Perform main tests

from catwigopy import Catwigopy

consumer_key, consumer_secret, access_token, access_token_secret = ["2eu2aB1DBgecsWPFmlbgIbuzO", "lUHC1VfcB958XwIBoyrgUsCA87iDrcXCy6lk6pwvhRnBzVrXZ6", "239585752-I06Pl7BzPC6Go3Qh1gLwKqUMzSvIgVi3ltjbzmwi", "pNyKGc5Jx3CSRKqnbB6LT8xO7AF2YSumDHQKrY8p7JIRj"]

cat = Catwigopy('Spotify', consumer_key, consumer_secret, access_token, access_token_secret)

cat.search_user_timeline(1200)
cat.classify_tweets_nmf()
print(cat.get_analysis_results())

