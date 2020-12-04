from unittest import TestCase
from day02.solution import read_pwd_line, check_sled_pwd_policy, check_toboggal_pwd_policy, count_valid_pwds


class TestSolution(TestCase):
    def test_read_pwd_line_example_1(self):
        test_line = '1-3 a: abcde'
        expected_result = (1, 3, 'a', 'abcde')
        self.assertTupleEqual(expected_result, read_pwd_line(test_line))

    def test_read_pwd_line_example_2(self):
        test_line = '1-3 b: cdefg'
        expected_result = (1, 3, 'b', 'cdefg')
        self.assertTupleEqual(expected_result, read_pwd_line(test_line))

    def test_read_pwd_line_example_3(self):
        test_line = '2-9 c: ccccccccc'
        expected_result = (2, 9, 'c', 'ccccccccc')
        self.assertTupleEqual(expected_result, read_pwd_line(test_line))

    def test_check_sled_pwd_policy_example_1(self):
        test_instance = (1, 3, 'a', 'abcde')
        self.assertTrue(check_sled_pwd_policy(*test_instance))

    def test_check_sled_pwd_policy_example_2(self):
        test_instance = (1, 3, 'b', 'cdefg')
        self.assertFalse(check_sled_pwd_policy(*test_instance))

    def test_check_sled_pwd_policy_example_3(self):
        test_instance = (2, 9, 'c', 'ccccccccc')
        self.assertTrue(check_sled_pwd_policy(*test_instance))

    def test_check_toboggal_pwd_policy_example_1(self):
        test_instance = (1, 3, 'a', 'abcde')
        self.assertTrue(check_toboggal_pwd_policy(*test_instance))

    def test_check_toboggal_pwd_policy_example_2(self):
        test_instance = (1, 3, 'b', 'cdefg')
        self.assertFalse(check_toboggal_pwd_policy(*test_instance))

    def test_check_toboggal_pwd_policy_example_3(self):
        test_instance = (2, 9, 'c', 'ccccccccc')
        self.assertFalse(check_toboggal_pwd_policy(*test_instance))

    def test_find_valid_pwds_example(self):
        test_instance = [
            '1-3 a: abcde',
            '1-3 b: cdefg',
            '2-9 c: ccccccccc'
        ]
        self.assertEqual(2, count_valid_pwds(test_instance))
