from unittest import TestCase
from unittest.mock import patch, mock_open
from day04.solution import read_input, parse_line


class TestSolution(TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='1\r\n2\r\n\r\n3')
    def test_read_input(self, m_open):
        result = read_input('/dummy/filename')
        m_open.assert_called_once_with('/dummy/filename')
        self.assertListEqual(['1\r\n2', '3'], result)

    def test_parse_lines_example_without_newline(self):
        test_line = 'byr:1991 eyr:2022 hcl:#341e13 iyr:2016 pid:729933757 hgt:167cm ecl:gry'
        expected_result = {
            'byr': '1991', 'eyr': '2022', 'hcl': '#341e13', 'iyr': '2016',
            'pid': '729933757', 'hgt': '167cm', 'ecl': 'gry'
        }
        self.assertDictEqual(expected_result, parse_line(test_line))

    def test_parse_lines_example_with_newline(self):
        test_line = 'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\r\nbyr:1937 iyr:2017 cid:147 hgt:183cm'
        expected_result = {
            'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd',
            'byr': '1937', 'iyr': '2017', 'cid': '147', 'hgt': '183cm'
        }
        self.assertDictEqual(expected_result, parse_line(test_line))
