
import unittest
from algorithm_collection.mathematics import lcm


class TestLCM(unittest.TestCase):
    def test_lcm(self):
        a, b = 15, 20
        self.assertEqual(lcm(a, b), 60)
