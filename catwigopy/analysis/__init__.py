

# Performs analysis using the provided nmf and tfidf model over the specified new doc.
# Returns a list containing the top 5 topics.
def apply_nmf(nmf, tfidf, tfidf_vectorizer, doc):
    # Transform vectorized tweet to NMF space
    nmf_new_doc = nmf.transform(tfidf_vectorizer.transform([doc]))
    # top 2 topics of the new feedback
    compo = nmf_new_doc.argsort()[0, :: -1]

    list_to_return = list()
    for topic_idx in compo:

        # Most probable topics:
        if nmf_new_doc[0][topic_idx] > 0.0:
            list_to_return.append(topic_idx)
    return list_to_return
