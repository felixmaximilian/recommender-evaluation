from unittest import TestCase
from recommender_kpi.evaluation import novelty_metric
import numpy as np

class TestNovelty(TestCase):
    def test_novelty_metric(self):
        recommendation_list = np.array([[0, 1, 2],
                                        [1, 2, 3]])
        self.assertAlmostEqual(novelty_metric(recommendation_list), 0.05)
