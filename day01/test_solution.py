import unittest
from unittest.mock import patch, mock_open
from day01.solution import get_expenses_report, find_pair_with_sum_2020, prefix_two_sum, prefix_three_sums


class TestSolution(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='1\n2\n3')
    def test_read_input_mock_open(self, m_open):
        result = get_expenses_report('/dummy/filename')
        m_open.assert_called_once_with('/dummy/filename')
        self.assertListEqual([1, 2, 3], result)

    @patch('builtins.open', new_callable=mock_open, read_data='1721\n979\n366\n299\n675\n1456')
    def test_read_input_example(self, m_open):
        result = get_expenses_report('/dummy/filename')
        m_open.assert_called_once_with('/dummy/filename')
        self.assertListEqual([1721, 979, 366, 299, 675, 1456], result)

    def test_find_pair_with_sum_2020_example(self):
        report = [1721, 979, 366, 299, 675, 1456]
        result = find_pair_with_sum_2020(report)
        self.assertTupleEqual((1721, 299), result)

    def test_find_pair_with_sum_2020_returns_None_if_there_is_none(self):
        report = [1, 2, 3]
        result = find_pair_with_sum_2020(report)
        self.assertIsNone(result)

    def test_prefix_two_sum_example(self):
        report = [1721, 979, 366, 299, 675, 1456]
        expected_result = [
            2700, 2087, 2020, 2396, 3177,
            1345, 1278, 1654, 2435,
            665, 1041, 1822,
            974, 1755,
            2131
        ]
        result = prefix_two_sum(report)
        self.assertListEqual(expected_result, result)

    def test_prefix_two_sum_small_example(self):
        report = [1, 2, 3]
        expected_result = [3, 4, 5]
        result = prefix_two_sum(report)
        self.assertListEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
