import unittest
import numpy as np
from recommender.autorec import custom_loss


class TestAutoRec(unittest.TestCase):
    y_true = np.array([1, 1, 1, 0, 0, 0])
    y_pred_1 = np.array([1, 1, 1, 0, 0, 0])
    y_pred_2 = np.array([0, 0, 0, 1, 1, 1])

    def test_custom_loss_0(self):
        expected = 0.0
        results = custom_loss(self.y_true, self.y_pred_1)
        self.assertTrue(expected, results)

    def test_custom_loss_1(self):
        expected = 1.0
        results = custom_loss(self.y_true, self.y_pred_2)
        self.assertTrue(expected, results)
