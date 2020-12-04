import re


def read_pwd_line(line):
    """Read a line of format '<num>-<num> <char>: <string>' and returns a tuple
       (int(num), int(num), char, string)"""
    result = re.split(r' |-|: ', line)
    min_limit, max_limit, *result = result
    return int(min_limit), int(max_limit), *result


def check_pwd_policy(min_limit, max_limit, char, pwd):
    pass
