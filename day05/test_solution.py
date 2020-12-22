from unittest import TestCase
from day05.solution import map_chars, decode_numbering, decode_seat_id


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
        self.mapped_rows = [44, 70, 14, 102]
        self.mapped_cols = [5, 7, 7, 4]
        self.row_coding = [64, 32, 16, 8, 4, 2, 1]
        self.col_coding = [4, 2, 1]

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

    def test_decode_numbering_for_rows_ex1(self):
        rows_to_decode = self.mapped_seat1[:-3]
        expected_result = decode_numbering(rows_to_decode, self.row_coding)
        self.assertEqual(self.mapped_rows[0], expected_result)

    def test_decode_numbering_for_rows_ex2(self):
        rows_to_decode = self.mapped_seat2[:-3]
        expected_result = decode_numbering(rows_to_decode, self.row_coding)
        self.assertEqual(self.mapped_rows[1], expected_result)

    def test_decode_numbering_for_rows_ex3(self):
        rows_to_decode = self.mapped_seat3[:-3]
        expected_result = decode_numbering(rows_to_decode, self.row_coding)
        self.assertEqual(self.mapped_rows[2], expected_result)

    def test_decode_numbering_for_rows_ex4(self):
        rows_to_decode = self.mapped_seat4[:-3]
        expected_result = decode_numbering(rows_to_decode, self.row_coding)
        self.assertEqual(self.mapped_rows[3], expected_result)

    def test_decode_numbering_for_cols_ex1(self):
        cols_to_decode = self.mapped_seat1[-3:]
        expected_result = decode_numbering(cols_to_decode, self.col_coding)
        self.assertEqual(self.mapped_cols[0], expected_result)

    def test_decode_numbering_for_cols_ex2(self):
        cols_to_decode = self.mapped_seat2[-3:]
        expected_result = decode_numbering(cols_to_decode, self.col_coding)
        self.assertEqual(self.mapped_cols[1], expected_result)

    def test_decode_numbering_for_cols_ex3(self):
        cols_to_decode = self.mapped_seat3[-3:]
        expected_result = decode_numbering(cols_to_decode, self.col_coding)
        self.assertEqual(self.mapped_cols[2], expected_result)

    def test_decode_numbering_for_cols_ex4(self):
        cols_to_decode = self.mapped_seat4[-3:]
        expected_result = decode_numbering(cols_to_decode, self.col_coding)
        self.assertEqual(self.mapped_cols[3], expected_result)

    def test_decode_seat_id_ex1(self):
        expected_result = (self.mapped_rows[0], self.mapped_cols[0])
        result = decode_seat_id(self.mapped_seat1, self.row_coding, self.col_coding)
        self.assertTupleEqual(expected_result, result)

    def test_decode_seat_id_ex2(self):
        expected_result = (self.mapped_rows[1], self.mapped_cols[1])
        result = decode_seat_id(self.mapped_seat2, self.row_coding, self.col_coding)
        self.assertTupleEqual(expected_result, result)

    def test_decode_seat_id_ex3(self):
        expected_result = (self.mapped_rows[2], self.mapped_cols[2])
        result = decode_seat_id(self.mapped_seat3, self.row_coding, self.col_coding)
        self.assertTupleEqual(expected_result, result)

    def test_decode_seat_id_ex4(self):
        expected_result = (self.mapped_rows[3], self.mapped_cols[3])
        result = decode_seat_id(self.mapped_seat4, self.row_coding, self.col_coding)
        self.assertTupleEqual(expected_result, result)
