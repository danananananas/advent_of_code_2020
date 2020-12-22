from unittest import TestCase
from unittest.mock import patch, mock_open
from day05.solution import (
    map_chars, decode_seat, decode_seat_id, decode_file,
    solution_part_1, partial_sum, solution_part_2
)


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
        self.seat_ids = [357, 567, 119, 820]

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

    def test_decode_seat_ex1(self):
        expected_result = (self.mapped_rows[0], self.mapped_cols[0])
        result = decode_seat(self.mapped_seat1)
        self.assertTupleEqual(expected_result, result)

    def test_decode_seat_ex2(self):
        expected_result = (self.mapped_rows[1], self.mapped_cols[1])
        result = decode_seat(self.mapped_seat2)
        self.assertTupleEqual(expected_result, result)

    def test_decode_seat_ex3(self):
        expected_result = (self.mapped_rows[2], self.mapped_cols[2])
        result = decode_seat(self.mapped_seat3)
        self.assertTupleEqual(expected_result, result)

    def test_decode_seat_ex4(self):
        expected_result = (self.mapped_rows[3], self.mapped_cols[3])
        result = decode_seat(self.mapped_seat4)
        self.assertTupleEqual(expected_result, result)

    def test_decode_seat_id_ex1(self):
        result = decode_seat_id(self.seat1, self.mapping)
        self.assertEqual(357, result)

    def test_decode_seat_id_ex2(self):
        result = decode_seat_id(self.seat2, self.mapping)
        self.assertEqual(567, result)

    def test_decode_seat_id_ex3(self):
        result = decode_seat_id(self.seat3, self.mapping)
        self.assertEqual(119, result)

    def test_decode_seat_id_ex4(self):
        result = decode_seat_id(self.seat4, self.mapping)
        self.assertEqual(820, result)

    @patch('builtins.open', new_callable=mock_open, read_data='FBFBBFFRLR\nBFFFBBFRRR\nFFFBBBFRRR\nBBFFBBFRLL')
    def test_decode_file(self, m_open):
        result = decode_file('/dummy/filename')
        self.assertListEqual(self.seat_ids, result)
        m_open.assert_called_once_with('/dummy/filename')

    def test_solution_part_1(self):
        self.assertEqual(820, solution_part_1(self.seat_ids))

    def test_partial_sum_from_1_to_10(self):
        result = partial_sum(1, 10)
        self.assertEqual(55, result)
        self.assertIsInstance(result, int)

    def test_partial_sum_one_element(self):
        result = partial_sum(1000, 1000)
        self.assertEqual(1000, result)
        self.assertIsInstance(result, int)

    def test_partial_sum_throws_exception_if_n_less_than_k(self):
        with self.assertRaisesRegex(ValueError, 'n can not be less than k'):
            partial_sum(2, 1)

    def test_solution_part_2_simple_example(self):
        result = solution_part_2([1, 2, 4, 5])
        self.assertEqual(3, result)

    def test_solution_part_2_more_complex_example(self):
        test_seat_ids = [*range(13, 42), *range(43, 67)]
        result = solution_part_2(test_seat_ids)
        self.assertEqual(42, result)
        self.assertIsInstance(result, int)


