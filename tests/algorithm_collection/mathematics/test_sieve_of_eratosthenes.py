import unittest
from algorithm_collection.mathematics import sieve_of_eratosthenes


class TestSieveOfEratosthenes(unittest.TestCase):
    def test_sieve_of_eratosthenes(self):
        n = 30
        res = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

        self.assertAlmostEqual(sieve_of_eratosthenes(n), res)
