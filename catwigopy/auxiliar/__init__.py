import spacy


def preprocess_tweets(tweets_array):
    nlp = spacy.load('en_core_web_sm')

    preprocessed_doc = list()

    for tweet in tweets_array:
        doc = nlp(tweet)
        [preprocessed_doc.append(token.lemma_.lower()) for token in doc if not token.is_stop and token.is_alpha and len(token.shape_) > 1]

    final_doc = " ".join(preprocessed_doc)

    return final_doc
