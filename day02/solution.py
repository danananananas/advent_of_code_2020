import operator
import re
from helper import read_input


def read_pwd_line(line):
    """Read a line of format '<num>-<num> <char>: <string>' and returns a tuple
       (int(num), int(num), char, string)"""
    result = re.split(r' |-|: ', line)
    first_num, second_num, *result = result
    return int(first_num), int(second_num), *result


def check_sled_pwd_policy(min_limit, max_limit, char, pwd):
    return min_limit <= pwd.count(char) <= max_limit


def check_toboggal_pwd_policy(first_index, second_index, char, pwd):
    return operator.xor(pwd[first_index - 1] == char, pwd[second_index - 1] == char)


def count_valid_pwds(lines, company):
    if company == 'sled':
        valid_pwds = (check_sled_pwd_policy(*read_pwd_line(line)) for line in lines)
    else:
        valid_pwds = (check_toboggal_pwd_policy(*read_pwd_line(line)) for line in lines)
    return sum(valid_pwds)


if __name__ == '__main__':
    print(count_valid_pwds(read_input('input.txt'), 'sled'))
    print(count_valid_pwds(read_input('input.txt'), 'toboggal'))
