from helper import read_input


def get_expenses_report(filename='input.txt'):
    report = read_input(filename)
    report = [int(expense) for expense in report]
    return report


def find_pair_with_sum_2020(report):
    pass
