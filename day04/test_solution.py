from unittest import TestCase
from unittest.mock import patch, mock_open

from day04.solution import read_input, parse_line, check_for_required_fields, check_input_for_required_fields
from day04.validation import (
    validate_byr, validate_iyr, validate_eyr, validate_hgt, validate_hcl,
    validate_ecl, validate_pid
)


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

    def test_check_input_for_required_fields_example(self):
        test_input = (
            'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\r\n'
            'byr:1937 iyr:2017 cid:147 hgt:183cm\r\n'
            '\r\n'
            'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884\r\n'
            'hcl:#cfa07d byr:1929\r\n'
            '\r\n'
            'hcl:#ae17e1 iyr:2013\r\n'
            'eyr:2024\r\n'
            'ecl:brn pid:760753108 byr:1931\r\n'
            'hgt:179cm\r\n'
            '\r\n'
            'hcl:#cfa07d eyr:2025 pid:166559648\r\n'
            'iyr:2011 ecl:brn hgt:59in'
        )
        expected_result = [True, False, True, False]
        with patch("builtins.open", mock_open(read_data=test_input)) as m_open:
            result = check_input_for_required_fields('/dummy/filename')
        m_open.assert_called_once_with('/dummy/filename')
        self.assertListEqual(expected_result, result)


class TestValidation(TestCase):
    def test_validate_byr_valid_year(self):
        self.assertTrue(validate_byr('2002'))

    def test_validate_byr_invalid_year_lt_1920(self):
        self.assertFalse(validate_byr('1919'))

    def test_validate_byr_invalid_year_gt_2002(self):
        self.assertFalse(validate_byr('2003'))

    def test_validate_byr_invalid_string(self):
        self.assertFalse(validate_byr('year'))

    def test_validate_iyr_valid_year(self):
        self.assertTrue(validate_iyr('2019'))

    def test_validate_iyr_invalid_year_lt_2010(self):
        self.assertFalse(validate_iyr('2009'))

    def test_validate_iyr_invalid_year_gt_2020(self):
        self.assertFalse(validate_iyr('2021'))

    def test_validate_iyr_invalid_string(self):
        self.assertFalse(validate_iyr('year'))

    def test_validate_eyr_valid_year(self):
        self.assertTrue(validate_eyr('2029'))

    def test_validate_eyr_invalid_year_lt_2020(self):
        self.assertFalse(validate_eyr('2009'))

    def test_validate_eyr_invalid_year_gt_2030(self):
        self.assertFalse(validate_eyr('2031'))

    def test_validate_eyr_invalid_string(self):
        self.assertFalse(validate_eyr('year'))

    def test_validate_hgt_valid_cm(self):
        self.assertTrue(validate_hgt('190cm'))

    def test_validate_hgt_valid_in(self):
        self.assertTrue(validate_hgt('60in'))

    def test_validate_hgt_invalid_cm_too_short(self):
        self.assertFalse(validate_hgt('149cm'))

    def test_validate_hgt_invalid_cm_too_high(self):
        self.assertFalse(validate_hgt('194cm'))

    def test_validate_hgt_invalid_in_too_short(self):
        self.assertFalse(validate_hgt('58in'))

    def test_validate_hgt_invalid_in_too_high(self):
        self.assertFalse(validate_hgt('77in'))

    def test_validate_hgt_invalid_missing_unit(self):
        self.assertFalse(validate_hgt('190'))

    def test_validate_hcl_valid(self):
        self.assertTrue(validate_hcl('#123abc'))

    def test_validate_hcl_invalid_char(self):
        self.assertFalse(validate_hcl('#123abz'))

    def test_validate_hcl_invalid_missing_pound_sign(self):
        self.assertFalse(validate_hcl('123abc'))

    def test_validate_hcl_invalid_too_short(self):
        self.assertFalse(validate_hcl('#12ab'))

    def test_validate_ecl_valid_all(self):
        for eye_colour in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            self.assertTrue(validate_ecl(eye_colour))

    def test_validate_ecl_invalid_colour(self):
        self.assertFalse(validate_ecl('grey'))

    def test_validate_pid_valid(self):
        self.assertTrue(validate_pid('896056539'))

    def test_validate_pid_valid_leading_zeros(self):
        self.assertTrue(validate_pid('000000001'))

    def test_validate_pid_invalid_too_long(self):
        self.assertFalse(validate_pid('0123456789'))

    def test_validate_pid_invalid_too_short(self):
        self.assertFalse(validate_pid('1234567'))

    def test_validate_pid_invalid_not_a_number(self):
        self.assertFalse(validate_pid('00000000l'))

