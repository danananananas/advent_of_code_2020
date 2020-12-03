import unittest
from unittest.mock import patch, mock_open
from helper import read_input


class TestFirst(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='1\n2\n3')
    def test_read_input(self, m_open):
        result = read_input()
        m_open.assert_called_once()
        self.assertListEqual(['1', '2', '3'], result)

    @patch('builtins.open', new_callable=mock_open, read_data='1 \n 2 \n 3\n')
    def test_read_input_strips_white_lines(self, m_open):
        result = read_input()
        m_open.assert_called_once()
        self.assertListEqual(['1', '2', '3'], result)


if __name__ == '__main__':
    unittest.main()
