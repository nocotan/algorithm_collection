
import unittest
from algorithm_collection.mathematics import gcd


class TestGCD(unittest.TestCase):
    def test_gcd(self):
        a, b = 15, 20
        self.assertEqual(gcd(a, b), 5)
