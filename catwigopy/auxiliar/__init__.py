import spacy


def preprocess_tweet(tweet):
        nlp = spacy.load('en_core_web_sm')

        tweet_ = nlp(tweet)

        preprocessed_tweet = ' '.join([token.lemma_.lower() for token in tweet_ if not token.is_stop and token.is_alpha and len(token.shape_) > 1])

        print(preprocessed_tweet)
        return preprocessed_tweet