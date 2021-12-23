import unittest

from .solution import part_1_solution, part_2_solution


class Day6TestCase(unittest.TestCase):
    def test_part_1(self):
        self.assertEqual(part_1_solution('16,1,2,0,4,2,7,1,2,14'), 37)

    def test_part_2(self):
        self.assertEqual(part_2_solution('16,1,2,0,4,2,7,1,2,14'), 168)