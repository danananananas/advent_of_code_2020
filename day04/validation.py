import re


def validate_byr(byr):
    try:
        return 1920 <= int(byr) <= 2002
    except ValueError:
        return False


def validate_iyr(iyr):
    try:
        return 2010 <= int(iyr) <= 2020
    except ValueError:
        return False


def validate_eyr(eyr):
    try:
        return 2020 <= int(eyr) <= 2030
    except ValueError:
        return False


def validate_hgt(hgt):
    if hgt[-2:] == 'cm':
        return 150 <= int(hgt[:-2]) <= 193
    elif hgt[-2:] == 'in':
        return 59 <= int(hgt[:-2]) <= 76
    else:
        return False


def validate_hcl(hcl):
    return re.match(r'^#[0-9a-f]{6}$', hcl) is not None


def validate_ecl(ecl):
    return ecl in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')


def validate_pid(pid):
    return re.match(r'^\d{9}$', pid) is not None
