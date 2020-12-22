from unittest import TestCase
from unittest.mock import patch, mock_open
from day06.solution import (
    count_unique_group_answers, count_all_unique_group_answers,
    count_only_answered_by_all_groups, count_all_only_answered_by_all_groups
)


class TestSolution(TestCase):
    def setUp(self):
        self.group1 = ['abc']
        self.group2 = ['a', 'b', 'c']
        self.group3 = ['ab', 'ac']
        self.group4 = ['a', 'a', 'a', 'a']
        self.group5 = ['b']
        self.groups = [self.group1, self.group2, self.group3, self.group4, self.group5]

    def test_count_unique_group_answers_ex1(self):
        self.assertEqual(3, count_unique_group_answers(self.group1))

    def test_count_unique_group_answers_ex2(self):
        self.assertEqual(3, count_unique_group_answers(self.group2))

    def test_count_unique_group_answers_ex3(self):
        self.assertEqual(3, count_unique_group_answers(self.group3))

    def test_count_unique_group_answers_ex4(self):
        self.assertEqual(1, count_unique_group_answers(self.group4))

    def test_count_unique_group_answers_ex5(self):
        self.assertEqual(1, count_unique_group_answers(self.group5))

    def test_count_only_answered_by_all_groups_ex1(self):
        self.assertEqual(3, count_only_answered_by_all_groups(self.group1))

    def test_count_only_answered_by_all_groups_ex2(self):
        self.assertEqual(0, count_only_answered_by_all_groups(self.group2))

    def test_count_only_answered_by_all_groups_ex3(self):
        self.assertEqual(1, count_only_answered_by_all_groups(self.group3))

    def test_count_only_answered_by_all_groups_ex4(self):
        self.assertEqual(1, count_only_answered_by_all_groups(self.group4))

    def test_count_only_answered_by_all_groups_ex5(self):
        self.assertEqual(1, count_only_answered_by_all_groups(self.group5))

    def test_count_all_unique_group_answers(self):
        result = count_all_unique_group_answers(self.groups)
        self.assertEqual(11, result)

    def test_count_all_only_answered_by_all_groups(self, ):
        result = count_all_only_answered_by_all_groups(self.groups)
        self.assertEqual(6, result)
