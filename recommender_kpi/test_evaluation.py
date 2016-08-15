from unittest import TestCase

from recommender_kpi.evaluation import novelty_metric, diversity_metric, degree_of_personalization, jaccard_distance
import numpy as np


class TestNovelty(TestCase):
    def test_novelty_metric(self):
        recommendation_list = np.array([[0, 1, 2],
                                        [1, 2, 3]])
        self.assertAlmostEqual(novelty_metric(recommendation_list),
                               (np.log2(2) + np.log2(2) + np.log2(2) + np.log2(2)) / (2 * 3))

    def test_diversity_metric(self):
        recommendation_list = np.array([[0, 1, 2],
                                        [1, 2, 3]])
        self.assertAlmostEqual(diversity_metric(recommendation_list), 2.0 / (np.sqrt(3) * np.sqrt(3)) / 2.0)

    def test_degree_of_personalization(self):
        top_n_recommendations = np.array([[0, 1, 2],
                                          [1, 2, 3]])
        set1 = set(top_n_recommendations[0, :])
        set2 = set(top_n_recommendations[1, :])
        print len(set1 & set2)
        print len(set1 | set2)
        self.assertAlmostEqual(degree_of_personalization(top_n_recommendations, fun=jaccard_distance),
                               1- (2.0 / 4.0))
