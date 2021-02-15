import unittest
from algorithm_collection.sort import sleep_sort


class TestSleepSort(unittest.TestCase):
    def test_sleep_sort(self):
        case_1 = [1, 3, 2, 4, 5]
        case_2 = [1, 2, 3, 4, 5]
        case_3 = [5, 4, 3, 2, 1]

        self.assertEqual(sleep_sort(case_1), sorted(case_1))
        self.assertEqual(sleep_sort(case_2), sorted(case_2))
        self.assertEqual(sleep_sort(case_3), sorted(case_3))
