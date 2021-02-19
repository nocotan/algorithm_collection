
import unittest
from algorithm_collection.sort import counting_sort


class TestCountingSort(unittest.TestCase):
    def test_counting_sort(self):
        case_1 = [1, 3, 2, 4, 5]
        case_2 = [1, 2, 3, 4, 5]
        case_3 = [5, 4, 3, 2, 1]

        self.assertEqual(counting_sort(case_1), sorted(case_1))
        self.assertEqual(counting_sort(case_2), sorted(case_2))
        self.assertEqual(counting_sort(case_3), sorted(case_3))
