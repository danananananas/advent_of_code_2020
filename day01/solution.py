from helper import read_input


def get_expenses_report (filename='input.txt'):
    report = read_input(filename)
    report = [int(expense) for expense in report]
    return report


def find_pair_with_sum_2020(report):
    for i, first_expense in enumerate(report):
        for second_expense in report[i + 1:]:
            if first_expense + second_expense == 2020:
                return first_expense, second_expense


def find_triple_with_sum_2020(report):
    for i, first_expense in enumerate(report[:-1]):
        for second_expense in report[i + 1:]:
            if (first_and_second := first_expense + second_expense) < 2020:
                remaining = 2020 - first_and_second
                if remaining in report:
                    return first_expense, second_expense, remaining


def first_solution():
    report = get_expenses_report()
    first_expense, second_expense = find_pair_with_sum_2020(report)
    return first_expense * second_expense


def second_solution():
    report = get_expenses_report()
    first_expense, second_expense, third_expense = find_triple_with_sum_2020(report)
    return first_expense * second_expense * third_expense


if __name__ == '__main__':
    print(first_solution())
    print(second_solution())
