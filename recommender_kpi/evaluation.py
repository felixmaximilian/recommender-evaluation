# Jaccard Distance
# https://de.wikipedia.org/wiki/Jaccard-Koeffizient
# 0.0 means both lists are equal

EPS = 1e-7

def jaccard_distance(id_list1, id_list2):
    assert len(id_list1) > 0 and len(id_list2) > 0, "first list has {} actions and second list has {} actions".format \
        (len(id_list1), len(id_list2))
    type_list1 = all(type(next(iter(id_list1))) == type(item) for item in id_list1)
    type_list2 = all(type(next(iter(id_list2))) == type(item) for item in id_list2)
    assert type_list1 and type_list2, 'not all ids have the same type, found in list1:{} in list2:{}'.format(type_list1,
                                                                                                             type_list2)
    assert type(next(iter(id_list1))) == type(next(iter(id_list2))), 'type mismatch between list1 and list2'

    set1 = set(id_list1)
    set2 = set(id_list2)
    if len(set1) > 0 & len(set2) > 0:
        return 1.0 - len(set1 & set2) / float(len(set1 + set2))
    else:
        return 1.0


def diversity_metric(bla, similarity_function='cosine'):
    return 0


def degree_of_personalization():
    return 0


# pop_dict can be an arbitrary count dict (e.g. number of contacts,views etc.)
# it defaults to the popularity inside the recommendations
# reference http://www.cs.ucl.ac.uk/fileadmin/UCL-CS/research/Research_Notes/RN_11_21.pdf
def novelty_metric(list_of_recommendations, pop_dict=None):
    from collections import Counter
    import numpy as np
    if not pop_dict:
        pop_dict = Counter(np.ravel(list_of_recommendations))
    novelty = 0.0
    for recommendations in list_of_recommendations:
        for recommendation in recommendations:
            novelty += np.log2(pop_dict.get(recommendation, default=1))  # log2(1) = 0

    return novelty / (list_of_recommendations.shape[0] * list_of_recommendations.shape[1])
