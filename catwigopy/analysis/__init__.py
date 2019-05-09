

# Performs analysis using the provided nmf and tfidf model over the specified new doc.
# Returns a list containing the non-0 topics and their score.
def apply_nmf(nmf, tfidf, tfidf_vectorizer, doc):
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

    # Transform vectorized tweet to NMF space
    nmf_new_doc = nmf.transform(tfidf_vectorizer.transform([doc]))
    compo = nmf_new_doc.argsort()[0, :: -1]

    # Get multiplicator to compute score
    l = [d for d in nmf_new_doc[0]]
    mult = 100 / sum(l)

    topic_list = list()
    score_list = list()
    for topic_idx in compo:
        # Most probable topics:
        if nmf_new_doc[0][topic_idx] > 0.0:
            topic_list.append(topic_idx)
            score_list.append(round(nmf_new_doc[0][topic_idx]*mult, 3))

    cat_list = list(map(lambda x: [pair[1] for pair in num_to_cat if pair[0] == x][0], topic_list))

    dict_to_return = dict(zip(cat_list, score_list))
    return dict_to_return
