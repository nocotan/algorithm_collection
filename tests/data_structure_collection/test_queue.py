
import unittest
from data_structure_collection import Queue


class TestQueue(unittest.TestCase):
    def test_queue(self):
        stack = Queue()
        for i in range(1, 11):
            stack.enqueue(i)

        for i in range(1, 11):
            x = stack.dequeue()
            self.assertEqual(x, i)
