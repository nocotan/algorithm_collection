import unittest
from algorithm_collection.geometry import circumference


class TestCircumference(unittest.TestCase):
    def test_circumference(self):
        r = 5
        self.assertAlmostEqual(31.41592653589793, circumference(r))
