from unittest import TestCase
from day03.solution import count_trees


class TestSolution(TestCase):
    def test_count_trees(self):
        test_lines = [
            '..##.......',
            '#...#...#..',
            '.#....#..#.',
            '..#.#...#.#',
            '.#...##..#.',
            '..#.##.....'
        ]
        self.assertEqual(3, count_trees(test_lines))
