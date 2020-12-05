from unittest import TestCase
from unittest.mock import patch, mock_open
from day04.solution import read_input, parse_line, check_for_required_fields, check_input_for_required_fields


class TestSolution(TestCase):
    test_input = (
        'byr:1991 eyr:2022 hcl:#341e13 iyr:2016 pid:729933757 hgt:167cm ecl:gry\n'
        '\n'
        'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\n'
        'byr:1937 iyr:2017 cid:147 hgt:183cm'
    )

    @patch('builtins.open', new_callable=mock_open, read_data=test_input)
    def test_read_input(self, m_open):
        expected_result = [
            {
                'byr': '1991', 'eyr': '2022', 'hcl': '#341e13', 'iyr': '2016',
                'pid': '729933757', 'hgt': '167cm', 'ecl': 'gry'
            },
            {
                'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd',
                'byr': '1937', 'iyr': '2017', 'cid': '147', 'hgt': '183cm'
            }
        ]
        result = read_input('/dummy/filename')
        m_open.assert_called_once_with('/dummy/filename')
        self.assertListEqual(expected_result, result)

    def test_parse_lines_example_without_newline(self):
        test_line = 'byr:1991 eyr:2022 hcl:#341e13 iyr:2016 pid:729933757 hgt:167cm ecl:gry'
        expected_result = {
            'byr': '1991', 'eyr': '2022', 'hcl': '#341e13', 'iyr': '2016',
            'pid': '729933757', 'hgt': '167cm', 'ecl': 'gry'
        }
        self.assertDictEqual(expected_result, parse_line(test_line))

    def test_parse_lines_example_with_newline(self):
        test_line = 'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\nbyr:1937 iyr:2017 cid:147 hgt:183cm'
        expected_result = {
            'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd',
            'byr': '1937', 'iyr': '2017', 'cid': '147', 'hgt': '183cm'
        }
        self.assertDictEqual(expected_result, parse_line(test_line))

    def test_check_for_required_fields_valid_passport(self):
        test_passport = {
            'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd',
            'byr': '1937', 'iyr': '2017', 'cid': '147', 'hgt': '183cm'
        }
        self.assertTrue(check_for_required_fields(test_passport))

    def test_check_for_required_fields_valid_no_cid(self):
        test_passport = {
            'byr': '1991', 'eyr': '2022', 'hcl': '#341e13', 'iyr': '2016',
            'pid': '729933757', 'hgt': '167cm', 'ecl': 'gry'
        }
        self.assertTrue(check_for_required_fields(test_passport))

    def test_check_for_required_fields_invalid(self):
        test_passport = {
            'iyr': '2013', 'ecl': 'amb', 'cid': '350', 'eyr': '2023',
            'pid': '028048884', 'hcl': '#cfa07d', 'byr': '1929'
        }
        self.assertFalse(check_for_required_fields(test_passport))

    @patch('builtins.open', new_callable=mock_open, read_data=test_input)
    def test_check_input_for_required_fields(self, m_open):
        result = check_input_for_required_fields('/dummy/filename')
        m_open.assert_called_once_with('/dummy/filename')
        self.assertListEqual([True, True], result)
