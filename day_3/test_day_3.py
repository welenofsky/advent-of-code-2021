import unittest

from .solution import part_1_solution, part_2_solution, get_most_significant_bit, get_least_significant_bit


class Day3TestCase(unittest.TestCase):
    def test_part_1(self):
        self.assertEqual(part_1_solution([
            '00100',
            '11110',
            '10110',
            '10111',
            '10101',
            '01111',
            '00111',
            '11100',
            '10000',
            '11001',
            '00010',
            '01010',
        ]), 198)

    def test_part_2(self):
        self.assertEqual(part_2_solution([
            '00100',
            '11110',
            '10110',
            '10111',
            '10101',
            '01111',
            '00111',
            '11100',
            '10000',
            '11001',
            '00010',
            '01010',
        ]), 230)

    def test_part_2_get_most_significant_bit(self):
        self.assertEqual(get_most_significant_bit([
            '00100',
            '11110',
            '10110',
            '10111',
            '10101',
            '01111',
            '00111',
            '11100',
            '10000',
            '11001',
            '00010',
            '01010',
        ], 0), '1')

        self.assertEqual(get_most_significant_bit([
            '11110',
            '10110',
            '10111',
            '10101',
            '11100',
            '10000',
            '11001',
        ], 1), '0')

        self.assertEqual(get_most_significant_bit([
            '10110',
            '10111',
            '10101',
            '10000',
        ], 2), '1')

        self.assertEqual(get_most_significant_bit([
            '10110',
            '10111',
            '10101',
        ], 3), '1')

        # When getting most significant and its even, go with '1'
        self.assertEqual(get_most_significant_bit([
            '10110',
            '10111',
        ], 4), '1')

    def test_part_2_get_least_significant_bit(self):
        self.assertEqual(get_least_significant_bit([
            '00100',
            '11110',
            '10110',
            '10111',
            '10101',
            '01111',
            '00111',
            '11100',
            '10000',
            '11001',
            '00010',
            '01010',
        ], 0), '0')

        self.assertEqual(get_least_significant_bit([
            '00100',
            '01111',
            '00111',
            '00010',
            '01010',
        ], 1), '1')

        # When getting most significant and its even, go with '0'
        self.assertEqual(get_least_significant_bit([
            '01111',
            '01010',
        ], 2), '0')
