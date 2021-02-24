import unittest
from algorithm_collection.mathematics import discriminant


class TestDiscriminant(unittest.TestCase):
    def test_discriminant(self):
        a = 20
        b = 30
        c = 10
        self.assertEqual(discriminant(a, b, c), 100)
