import re


def read_input(filename):
    with open(filename) as f:
        return re.split('\r\n\r\n|\n\n', f.read())


def parse_line(line):
    items = re.split(' |\r\n|\n', line)
    # noinspection PyTypeChecker
    items = dict(item.split(':') for item in items)
    return items
