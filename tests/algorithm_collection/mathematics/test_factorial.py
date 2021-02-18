import unittest
from algorithm_collection.mathematics import factorial


class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
