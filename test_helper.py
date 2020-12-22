import unittest
from unittest.mock import patch, mock_open
from helper import read_input, read_input_w_double_return


class TestFirst(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='1\n2\n3')
    def test_read_input(self, m_open):
        result = read_input('/dummy/filename')
        m_open.assert_called_once_with('/dummy/filename')
        self.assertListEqual(['1', '2', '3'], result)

    @patch('builtins.open', new_callable=mock_open, read_data='1 \n 2 \n 3\n')
    def test_read_input_strips_white_lines(self, m_open):
        result = read_input('/dummy/filename')
        m_open.assert_called_once_with('/dummy/filename')
        self.assertListEqual(['1', '2', '3'], result)

    @patch('builtins.open', new_callable=mock_open, read_data='1\n\n2\n1\n3\n\n1\n2\n3')
    def test_read_input_w_double_return(self, m_open):
        result = read_input_w_double_return('/dummy/filename')
        m_open.assert_called_once_with('/dummy/filename')
        self.assertListEqual([['1'], ['2', '1', '3'], ['1', '2', '3']], result)


if __name__ == '__main__':
    unittest.main()
