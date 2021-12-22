import unittest

from .solution import part_1_solution, part_2_solution


class Day2TestCase(unittest.TestCase):
    def test_part_1(self):
        self.assertEqual(part_1_solution([
            'forward 5',
            'down 5',
            'forward 8',
            'up 3',
            'down 8',
            'forward 2'
        ]), 150)

    def test_part_2(self):
        self.assertEqual(part_2_solution([
            'forward 5',
            'down 5',
            'forward 8',
            'up 3',
            'down 8',
            'forward 2'
        ]), 900)