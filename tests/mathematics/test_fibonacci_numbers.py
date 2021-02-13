
import unittest
from algorithm_collection.mathematics import fibonacci_numbers


class TestFibonacciNumbers(unittest.TestCase):
    def test_fibonacci_numbers(self):
        case_1 = {"n": 0, "output": 0}
        case_2 = {"n": 1, "output": 1}
        case_3 = {"n": 2, "output": 1}
        case_4 = {"n": 3, "output": 2}
        case_5 = {"n": 4, "output": 3}
        case_6 = {"n": 5, "output": 5}
        case_7 = {"n": 6, "output": 8}
        case_8 = {"n": 7, "output": 13}

        self.assertEqual(fibonacci_numbers(case_1["n"]), case_1["output"])
        self.assertEqual(fibonacci_numbers(case_2["n"]), case_2["output"])
        self.assertEqual(fibonacci_numbers(case_3["n"]), case_3["output"])
        self.assertEqual(fibonacci_numbers(case_4["n"]), case_4["output"])
        self.assertEqual(fibonacci_numbers(case_5["n"]), case_5["output"])
        self.assertEqual(fibonacci_numbers(case_6["n"]), case_6["output"])
        self.assertEqual(fibonacci_numbers(case_7["n"]), case_7["output"])
        self.assertEqual(fibonacci_numbers(case_8["n"]), case_8["output"])
