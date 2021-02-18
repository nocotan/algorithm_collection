import unittest
from algorithm_collection.search import binary_search


class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        case_1 = {"arr": [1, 3, 2, 4, 5], "key": 4}
        case_2 = {"arr": [1, 2, 3, 4, 4], "key": 4}
        case_3 = {"arr": [1, 2, 3, 4, 5], "key": 1}
        case_4 = {"arr": [1, 2, 3, 4, 5], "key": 5}
        case_5 = {"arr": [1, 2, 3, 4, 5], "key": 6}

        self.assertEqual(binary_search(case_1["arr"], case_1["key"]),
                         case_1["arr"].index(case_1["key"]))
        self.assertEqual(binary_search(case_2["arr"], case_2["key"]),
                         case_2["arr"].index(case_2["key"]))
        self.assertEqual(binary_search(case_3["arr"], case_3["key"]),
                         case_3["arr"].index(case_3["key"]))
        self.assertEqual(binary_search(case_4["arr"], case_4["key"]),
                         case_4["arr"].index(case_4["key"]))
        self.assertEqual(binary_search(case_5["arr"], case_5["key"]), -1)
