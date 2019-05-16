import spacy


def preprocess_tweet(tweet):
        nlp = spacy.load('en_core_web_sm')

        tweet_ = nlp(tweet)
        prep = [token.lemma_.lower() for token in tweet_ if not token.is_stop and token.is_alpha and len(token.shape_) > 1]

        preprocessed_tweet = ' '.join(prep)
        preprocessed_tokens = prep

        return preprocessed_tweet, preprocessed_tokens
