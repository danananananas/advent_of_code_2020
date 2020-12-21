from unittest import TestCase
from day05.solution import decode_row, map_chars


class SolutionTest(TestCase):
    def setUp(self):
        self.seat1 = 'FBFBBFFRLR'
        self.seat2 = 'BFFFBBFRRR'
        self.seat3 = 'FFFBBBFRRR'
        self.seat4 = 'BBFFBBFRLL'
        self.mapped_seat1 = '0101101101'
        self.mapped_seat2 = '1000110111'
        self.mapped_seat3 = '0001110111'
        self.mapped_seat4 = '1100110100'

    def test_map_chars_ex1(self):
        self.assertEqual(self.mapped_seat1, map_chars(self.seat1))

    def test_map_chars_ex2(self):
        self.assertEqual(self.mapped_seat2, map_chars(self.seat2))

    def test_map_chars_ex3(self):
        self.assertEqual(self.mapped_seat3, map_chars(self.seat3))

    def test_map_chars_ex4(self):
        self.assertEqual(self.mapped_seat4, map_chars(self.seat4))

    def test_decode_row_ex1(self):
        pass
