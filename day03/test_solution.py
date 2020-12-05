from unittest import TestCase
from day03.solution import count_trees


class TestSolution(TestCase):
    def setUp(self):
        self.test_lines = [
            '..##.......',
            '#...#...#..',
            '.#....#..#.',
            '..#.#...#.#',
            '.#...##..#.',
            '..#.##.....'
        ]

    def test_count_trees_right_3_down_1(self):
        self.assertEqual(3, count_trees(self.test_lines, right=3))

    def test_count_trees_right_3_down_2(self):
        self.assertEqual(1, count_trees(self.test_lines, right=3, down=2))
