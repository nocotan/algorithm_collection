import unittest
from data_structure_collection import Stack


class TestStack(unittest.TestCase):
    def test_stack(self):
        stack = Stack()
        for i in range(1, 11):
            stack.push(i)

        for i in range(1, 11):
            remove = stack.pop()
            self.assertEqual(remove, 11-i)
