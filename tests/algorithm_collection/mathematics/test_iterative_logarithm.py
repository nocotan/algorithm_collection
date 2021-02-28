import unittest
from algorithm_collection.mathematics import iterative_logarithm


class TestIterativeLogarithm(unittest.TestCase):
    def test_iterative_logarithm(self):
        n = 100
        base = 5
        self.assertEqual(iterative_logarithm(n, base), 2)
