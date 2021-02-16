import unittest
from scipy.spatial import distance
from distance_collection import cosine_distance


class TestCosineDistance(unittest.TestCase):
    def test_cosine_distance(self):
        a = [1, 2, 3, 4, 5]
        b = [2, 4, 6, 8, 10]

        self.assertEqual(cosine_distance(a, b), distance.cosine(a, b))
