import re
from helper import read_input


def read_pwd_line(line):
    """Read a line of format '<num>-<num> <char>: <string>' and returns a tuple
       (int(num), int(num), char, string)"""
    result = re.split(r' |-|: ', line)
    min_limit, max_limit, *result = result
    return int(min_limit), int(max_limit), *result


def check_pwd_policy(min_limit, max_limit, char, pwd):
    return min_limit <= pwd.count(char) <= max_limit


def count_valid_pwds(lines):
    valid_pwds = [check_pwd_policy(*read_pwd_line(line)) for line in lines]
    return sum(valid_pwds)


if __name__ == '__main__':
    print(count_valid_pwds(read_input('input.txt')))
