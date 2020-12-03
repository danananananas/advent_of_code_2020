import unittest
from unittest.mock import patch, mock_open
from day01.solution import get_expenses_report, find_pair_with_sum_2020


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


if __name__ == '__main__':
    unittest.main()
