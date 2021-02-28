import unittest
from algorithm_collection.mathematics import correlation_coefficient


class TestCorrelationCoefficient(unittest.TestCase):
    def test_correlation_coefficient(self):
        X = [15, 18, 21, 24, 27]
        Y = [25, 25, 27, 31, 32]

        self.assertAlmostEqual(correlation_coefficient(X, Y), 0.953463, 6)
