import unittest
from algorithm_collection.geometry import arc_length


class TestArcLength(unittest.TestCase):
    def test_arc_length(self):
        diameter = 25.0
        angle = 45.0
        self.assertAlmostEqual(arc_length(diameter, angle), 9.817477042468104)
