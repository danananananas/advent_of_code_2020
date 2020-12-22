import re


def read_input(filename):
    with open(filename) as f:
        return [line.strip() for line in f]


def read_input_w_double_return(filename):
    with open(filename) as f:
        lines = re.split('\r\n\r\n|\n\n', f.read())
        lines = [re.split(' |\r\n|\n', line) for line in lines]
        return lines
