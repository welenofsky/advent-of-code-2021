import unittest

from .solution import part_1_solution, part_2_solution


class Day2TestCase(unittest.TestCase):
    def test_part_1(self):
        self.assertEqual(part_1_solution([
            '199',
            '200',
            '208',
            '210',
            '200',
            '207',
            '240',
            '269',
            '260',
            '263',
        ]), 7)

    def test_part_2(self):
        self.assertEqual(part_2_solution([
            '607',
            '618',
            '618',
            '617',
            '647',
            '716',
            '769',
            '792',
        ]), 5)