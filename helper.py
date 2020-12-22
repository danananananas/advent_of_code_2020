import re


def read_input(filename):
    with open(filename) as f:
        return [line.strip() for line in f]


def read_input_w_double_return(filename):
    with open(filename) as f:
        lines = re.split('\n\n', f.read())
        lines = [line.replace('\n', '') for line in lines]
        return lines


def read_input_w_double_n_single_return(filename):
    with open(filename) as f:
        lines = re.split('\n\n', f.read())
        lines = [re.split(' |\n', line) for line in lines]
        return lines
