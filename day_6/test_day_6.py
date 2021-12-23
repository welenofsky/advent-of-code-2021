import unittest

from .solution import part_1_solution


class Day6TestCase(unittest.TestCase):
    def test_part_1(self):
        self.assertEqual(part_1_solution('3,4,3,1,2'), 5934)
