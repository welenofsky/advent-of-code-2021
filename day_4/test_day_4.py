import unittest

from .game import Board
from .solution import part_1_solution, part_2_solution


class Day4TestCase(unittest.TestCase):
    def test_board_score_calculation(self):
        data = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]
        board = Board(data)
        board.data[0][0].marked = True

        self.assertEqual(board.get_score(), 77)

        board.data[0][1].marked = True

        self.assertEqual(board.get_score(), 75)

    def test_part_1(self):
        self.assertEqual(part_1_solution([
            '7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1',
            '',
            '22 13 17 11  0',
            '8  2 23  4 24',
            '21  9 14 16  7',
            '6 10  3 18  5',
            '1 12 20 15 19',
            '',
            '3 15  0  2 22',
            '9 18 13 17  5',
            '19  8  7 25 23',
            '20 11 10 24  4',
            '14 21 16 12  6',
            '',
            '14 21 17 24  4',
            '10 16 15  9 19',
            '18  8 23 26 20',
            '22 11 13  6  5',
            '2  0 12  3  7',
        ]), 4512)

    def test_part_2(self):
        self.assertEqual(part_2_solution([
            '7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1',
            '',
            '22 13 17 11  0',
            '8  2 23  4 24',
            '21  9 14 16  7',
            '6 10  3 18  5',
            '1 12 20 15 19',
            '',
            '3 15  0  2 22',
            '9 18 13 17  5',
            '19  8  7 25 23',
            '20 11 10 24  4',
            '14 21 16 12  6',
            '',
            '14 21 17 24  4',
            '10 16 15  9 19',
            '18  8 23 26 20',
            '22 11 13  6  5',
            '2  0 12  3  7',
            ''
        ]), 1924)