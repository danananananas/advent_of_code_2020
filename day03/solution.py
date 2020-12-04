def count_trees(lines):
    counter = 0
    n = len(lines[0])
    for i, line in enumerate(lines):
        if line[3 * i % n] == '#':
            counter += 1
    return counter
