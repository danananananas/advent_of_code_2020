from unittest import TestCase
from unittest.mock import patch, mock_open
from day04.solution import read_input


class TestSolution(TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='1\n2\n\n3')
    def test_read_input(self, m_open):
        result = read_input('/dummy/filename')
        m_open.assert_called_once_with('/dummy/filename')
        self.assertListEqual(['1\n2', '3'], result)
