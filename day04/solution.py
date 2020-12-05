import re


def read_input(filename):
    with open(filename) as f:
        return re.split('\r\n\r\n|\n\n', f.read())


def parse_line(line):
    line = re.split(' |\r\n|\n', line)
    return line
