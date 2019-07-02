import gensim.corpora as corpora

num_to_cat = [(0, 'Music and Radio'),
                  (1, 'Movies'),
                  (2, 'Videogames'),
                  (3, 'Books and Literature'),
                  (4, 'Careers'),
                  (5, 'Personal Health'),
                  (6, 'Religion and Spirituality'),
                  (7, 'Home and Garden'),
                  (8, 'Personal Finance'),
                  (9, 'Pets and Animals'),
                  (10, 'Shopping'),
                  (11, 'Travel'),
                  (12, 'Automotive'),
                  (13, 'Fine Art'),
                  (14, 'Science'),
                  (15, 'News and Politics'),
                  (16, 'Education'),
                  (17, 'Food and Drink'),
                  (18, 'Financial and Business'),
                  (19, 'Family and Relationships'),
                  (20, 'Style and Fashion'),
                  (21, 'Medical Health'),
                  (22, 'Software and Technology'),
                  (23, 'Events'),
                  (24, 'Hobbies and Pop Culture'),
                  (25, 'Sports'),
                  (26, 'trash'),
                  (27, 'trash'),
                  (28, 'trash'),
                  (None, 'None')]


def apply_nmf(nmf, tfidf, tfidf_vectorizer, doc):

    """
    This function performs user's tweets analysis.

    :param nmf: nmf model trained.
    :param tfidf: tfidf dictionary.
    :param tfidf_vectorizer: tfidf model trained.
    :param doc: string containing all the user's tweets joined.
    :return: dictionary of shape {category_name: score}
    """

    # Transform vectorized tweet to NMF space
    nmf_new_doc = nmf.transform(tfidf_vectorizer.transform([doc]))
    compo = nmf_new_doc.argsort()[0, :: -1]

    # Get multiplicator to compute score
    mul = 100 / sum([d for d in nmf_new_doc[0]])

    topic_list = list()
    score_list = list()
    for topic_idx in compo:
        # Most probable topics:
        if nmf_new_doc[0][topic_idx] > 0.0:
            topic_list.append(topic_idx)
            score_list.append(round(nmf_new_doc[0][topic_idx]*mul, 3))

    cat_list = list(map(lambda x: [pair[1] for pair in num_to_cat if pair[0] == x][0], topic_list))

    dict_to_return = dict(zip(cat_list, score_list))
    return dict_to_return


# Takes as imput a list of lists containing terms and returns a dictionary type:
# [{
#     'text': 'term',
#     'count': 2
# }, ...]
def generate_occurences_dictionay(list):

    """
    This function counts the occurrences of each term in a list.

    :param list: list of hashtags / tweets

    :return: list of shape [{text: term, count: occurrences}]
    """

    dictionary = corpora.Dictionary(list)

    terms_with_score = []
    for word, id_ in dictionary.token2id.items():
        temp = {
            'text':  word,
            'count': dictionary.dfs[id_]
        }
        terms_with_score.append(temp)

    return terms_with_score


def generate_top_terms_dictionary(nmf, tfidf_vectorizer, nterms=30):

    """
    This function extract the top terms of each topic in the nmf trained model.

    :param nmf: nmf model trained
    :param tfidf_vectorizer: tfidf model trained
    :param nterms: Number of top terms to retrieve.

    :return: dictionary of shape {category_name: [{text: term_name, values: term_score}]}
    """

    all_topics_dict = dict()
    fnames = tfidf_vectorizer.get_feature_names()

    for topic_idx, topic in enumerate(nmf.components_):
        name = num_to_cat[topic_idx][1]
        if name and name is not 'trash':
            all_topics_dict[name] = [{'text': fnames[t], 'values': float("{0:.3f}".format(topic[t]/sum(topic)*100))} for t in topic.argsort()[:-nterms - 1:-1]]

    return all_topics_dict
