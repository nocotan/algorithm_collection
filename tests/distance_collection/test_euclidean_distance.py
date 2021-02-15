import unittest
from scipy.spatial import distance
from distance_collection import euclidean_distance


class TestEuclideanDistance(unittest.TestCase):
    def test_euclidean_distance(self):
        a = [1, 2, 3, 4, 5]
        b = [2, 4, 6, 8, 10]

        self.assertEqual(euclidean_distance(a,b), distance.euclidean(a,b))
