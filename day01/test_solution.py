import unittest
from unittest.mock import patch, mock_open
from solution import get_expenses_report


class TestSolution(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='1\n2\n3')
    def test_read_input(self, m_open):
        result = get_expenses_report('/dummy/filename')
        m_open.assert_called_once_with('/dummy/filename')
        self.assertListEqual([1, 2, 3], result)


if __name__ == '__main__':
    unittest.main()
