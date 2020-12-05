import math
from helper import read_input


def count_trees(lines, right, down=1):
    counter = 0
    n = len(lines[0])
    for i, line in enumerate(lines[::down]):
        if line[right * i % n] == '#':
            counter += 1
    return counter


if __name__ == '__main__':
    area = read_input('input.txt')
    print(count_trees(area, 3))
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    trees = [count_trees(area, right, down) for right, down in slopes]
    print(math.prod(trees))
