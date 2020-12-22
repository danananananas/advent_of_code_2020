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

    @patch('builtins.open', new_callable=mock_open, read_data='abc\n\na\nb\nc\n\nab\nac\n\na\na\na\na\n\nb')
    def test_count_all_unique_group_answers(self, m_open):
        result = count_all_unique_group_answers('/dummy/filename')
        m_open.assert_called_once_with('/dummy/filename')
        self.assertListEqual([3, 3, 3, 1, 1], result)

    @patch('builtins.open', new_callable=mock_open, read_data='abc\n\na\nb\nc\n\nab\nac\n\na\na\na\na\n\nb')
    def test_count_all_only_answered_by_all_groups(self, m_open):
        result = count_all_only_answered_by_all_groups('/dummy/filename')
        m_open.assert_called_once_with('/dummy/filename')
        self.assertListEqual([3, 0, 1, 1, 1], result)
