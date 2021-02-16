import unittest
from scipy.spatial import distance
from distance_collection import canberra_distance


class TestCosineCanberraDistance(unittest.TestCase):
    def test_canberra_distance(self):
        a = [1, 2, 3, 4, 5]
        b = [2, 4, 6, 8, 10]

        self.assertEqual(canberra_distance(a, b), distance.canberra(a, b))
