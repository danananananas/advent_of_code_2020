from unittest import TestCase
from day05.solution import decode_row, map_chars


class SolutionTest(TestCase):
    def setUp(self):
        self.mapping = {'F': '0', 'B': '1', 'L': '0', 'R': '1'}
        self.seats = 'FBFBBFFRLR\nBFFFBBFRRR\nFFFBBBFRRR\nBBFFBBFRLL'
        self.seat1 = 'FBFBBFFRLR'
        self.seat2 = 'BFFFBBFRRR'
        self.seat3 = 'FFFBBBFRRR'
        self.seat4 = 'BBFFBBFRLL'
        self.mapped_seats = '0101100101\n1000110111\n0001110111\n1100110100'
        self.mapped_seat1 = '0101100101'
        self.mapped_seat2 = '1000110111'
        self.mapped_seat3 = '0001110111'
        self.mapped_seat4 = '1100110100'

    def test_map_chars_ex1(self):
        self.assertEqual(self.mapped_seat1, map_chars(self.seat1, self.mapping))

    def test_map_chars_ex2(self):
        self.assertEqual(self.mapped_seat2, map_chars(self.seat2, self.mapping))

    def test_map_chars_ex3(self):
        self.assertEqual(self.mapped_seat3, map_chars(self.seat3, self.mapping))

    def test_map_chars_ex4(self):
        self.assertEqual(self.mapped_seat4, map_chars(self.seat4, self.mapping))

    def test_map_chars_4_seats(self):
        self.assertEqual(self.mapped_seats, map_chars(self.seats, self.mapping))

    def test_map_chars_different_mapping(self):
        chars_to_map = 'danananananas'
        expected_map = 'dnananananans'
        mapping = {'n': 'a', 'a': 'n'}
        self.assertEqual(expected_map, map_chars(chars_to_map, mapping))

    def test_map_chars_raises_exception_when_mapping_is_not_dict(self):
        with self.assertRaises(TypeError):
            map_chars(self.seats, ['0', '1'])

    def test_map_chars_does_not_work_without_mapping(self):
        with self.assertRaises(TypeError):
            self.assertEqual(self.mapped_seats, map_chars(self.seats))

    def test_decode_row_ex1(self):
        pass
