import unittest
from algorithm_collection.mathematics import sieve_of_sundaram


class TestSieveOfSundaram(unittest.TestCase):
    def test_sieve_of_sundaram(self):
        n = 30
        res = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

        self.assertAlmostEqual(sieve_of_sundaram(n), res)
