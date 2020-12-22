from unittest import TestCase
from day06.solution import count_unique_group_answers


class TestSolution(TestCase):
    def test_check_group_answers_ex1(self):
        test_group = ['abc']
        self.assertEqual(3, count_unique_group_answers(test_group))

    def test_check_group_answers_ex2(self):
        test_group = ['abac']
        self.assertEqual(3, count_unique_group_answers(test_group))

    def test_check_group_answers_ex3(self):
        test_group = ['aaaa']
        self.assertEqual(1, count_unique_group_answers(test_group))

    def test_check_group_answers_ex4(self):
        test_group = ['b']
        self.assertEqual(1, count_unique_group_answers(test_group))
