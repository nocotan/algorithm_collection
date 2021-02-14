import unittest
import numpy as np

from algorithm_collection.mathematics import prime_factors


class TestPrimeNumbers(unittest.TestCase):
    def test_prime_numbers(self):
        n = 315
        res = [3, 3, 5, 7]

        self.assertTrue(np.array_equal(prime_factors(n), res))
