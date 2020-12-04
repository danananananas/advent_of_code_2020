from unittest import TestCase
from day02.solution import read_pwd_line, check_pwd_policy


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

    def test_check_pwd_policy_example_1(self):
        test_instance = (1, 3, 'a', 'abcde')
        self.assertTrue(check_pwd_policy(*test_instance))

    def test_check_pwd_policy_example_2(self):
        test_instance = (1, 3, 'b', 'cdefg')
        self.assertFalse(check_pwd_policy(*test_instance))

    def test_check_pwd_policy_example_3(self):
        test_instance = (2, 9, 'c', 'ccccccccc')
        self.assertTrue(check_pwd_policy(*test_instance))
