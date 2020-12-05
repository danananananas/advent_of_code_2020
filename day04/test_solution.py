from unittest import TestCase
from unittest.mock import patch, mock_open
from day04.solution import read_input, parse_lines


class TestSolution(TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='1\r\n2\r\n\r\n3')
    def test_read_input(self, m_open):
        result = read_input('/dummy/filename')
        m_open.assert_called_once_with('/dummy/filename')
        self.assertListEqual(['1\r\n2', '3'], result)

    def test_parse_lines(self):
        test_lines = ['1\r\n2', '3']
        expected_result = [['1', '2'], ['3']]
        self.assertListEqual(expected_result, parse_lines(test_lines))
