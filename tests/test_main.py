#Perform main tests

from twitterpreferencesprofile.twitter_retriever.tcrawler import TCrawler

myT1 = TCrawler()
myT2 = TCrawler()

myT1.search(query='hola', lang='es', number=1)
myT2.search(query='adios', lang='es', number=1)
