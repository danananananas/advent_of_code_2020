from unittest import TestCase
from unittest.mock import patch, mock_open
from day06.solution import (
    count_unique_group_answers, count_all_unique_group_answers,
    count_only_answered_by_all_groups, count_all_only_answered_by_all_groups
)


class TestSolution(TestCase):
    def test_count_unique_group_answers_ex1(self):
        test_group = 'abc'
        self.assertEqual(3, count_unique_group_answers(test_group))

    def test_count_unique_group_answers_ex2(self):
        test_group = 'abac'
        self.assertEqual(3, count_unique_group_answers(test_group))

    def test_count_unique_group_answers_ex3(self):
        test_group = 'aaaa'
        self.assertEqual(1, count_unique_group_answers(test_group))

    def test_count_unique_group_answers_ex4(self):
        test_group = 'b'
        self.assertEqual(1, count_unique_group_answers(test_group))

    def test_count_only_answered_by_all_groups_ex1a(self):
        test_group = ['abc']
        self.assertEqual(3, count_only_answered_by_all_groups(test_group))

    def test_count_only_answered_by_all_groups_ex1b(self):
        test_group = ['a', 'b', 'c']
        self.assertEqual(0, count_only_answered_by_all_groups(test_group))

    def test_count_only_answered_by_all_groups_ex2(self):
        test_group = ['ab', 'ac']
        self.assertEqual(1, count_only_answered_by_all_groups(test_group))

    def test_count_only_answered_by_all_groups_ex3(self):
        test_group = ['a', 'a', 'a', 'a']
        self.assertEqual(1, count_only_answered_by_all_groups(test_group))

    def test_count_only_answered_by_all_groups_ex4(self):
        test_group = ['b']
        self.assertEqual(1, count_only_answered_by_all_groups(test_group))

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
