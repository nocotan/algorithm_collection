import unittest
from algorithm_collection.mathematics import exponential_taylor_approximation


class TestExponential(unittest.TestCase):
    def test_exponential_taylor_approximation(self):
        n = 10
        x = 1.0

        self.assertEqual(exponential_taylor_approximation(x, n), 2.7182818011463845)
