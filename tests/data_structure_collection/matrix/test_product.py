import unittest
import numpy as np

from data_structure_collection.matrix import product


class TestProduct(unittest.TestCase):
    def test_product(self):
        mat1 = [[2, 4], [3, 4]]
        mat2 = [[1, 2], [1, 3]]
        m1, m2, n1, n2 = 2, 2, 2, 2

        res = product(m1, m2, mat1, n1, n2, mat2)
        self.assertTrue(np.array_equal(np.array(res), np.dot(mat1, mat2)))
