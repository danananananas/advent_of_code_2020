import re
from helper import read_input_w_double_n_single_return
from day04.validation import (
    validate_byr, validate_iyr, validate_eyr, validate_hgt, validate_hcl,
    validate_ecl, validate_pid
)


validate_methods = {
    'byr': validate_byr, 'iyr': validate_iyr, 'eyr': validate_eyr,
    'hgt': validate_hgt, 'hcl': validate_hcl, 'ecl': validate_ecl,
    'pid': validate_pid
}


def read_n_parse_input(filename):
    lines = read_input_w_double_n_single_return(filename)
    return [parse_line(line) for line in lines]


def parse_line(line):
    items = re.split(' |\r\n|\n', line)
    # noinspection PyTypeChecker
    items = dict(item.split(':') for item in items)
    return items


def check_for_required_fields(passport):
    required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    return required_fields.issubset(set(passport.keys()))


def check_input_for_required_fields(passports):
    return [check_for_required_fields(passport) for passport in passports]


def validate(passport):
    required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    for required_field in required_fields:
        try:
            if not validate_methods[required_field](passport[required_field]):
                return False
        except KeyError:
            return False
    return True


def validate_input(passports):
    return [validate(passport) for passport in passports]


if __name__ == '__main__':
    input_passports = read_input('input.txt')
    print(sum(check_input_for_required_fields(input_passports)))
    print(sum(validate_input(input_passports)))
