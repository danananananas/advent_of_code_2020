import re


def read_input(filename):
    with open(filename) as f:
        lines = re.split('\r\n\r\n|\n\n', f.read())
        return [parse_line(line) for line in lines]


def parse_line(line):
    items = re.split(' |\r\n|\n', line)
    # noinspection PyTypeChecker
    items = dict(item.split(':') for item in items)
    return items


def check_for_required_fields(passport):
    required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    return required_fields.issubset(set(passport.keys()))


def check_input_for_required_fields(filename):
    passports = read_input(filename)
    return [check_for_required_fields(passport) for passport in passports]


if __name__ == '__main__':
    print(sum(check_input_for_required_fields('input.txt')))
