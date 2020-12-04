from helper import read_input


def count_trees(lines, right):
    counter = 0
    n = len(lines[0])
    for i, line in enumerate(lines):
        if line[right * i % n] == '#':
            counter += 1
    return counter


if __name__ == '__main__':
    print(count_trees(read_input('input.txt'), 3))
