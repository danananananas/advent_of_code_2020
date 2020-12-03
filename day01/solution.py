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


def first_solution():
    report = get_expenses_report()
    first_expense, second_expense = find_pair_with_sum_2020(report)
    return first_expense * second_expense


def prefix_two_sum(report):
    pairs_sums = []
    for i, first_expense in enumerate(report):
        for j, second_expense in enumerate(report[i+1:], start=i+1):
            pairs_sums.append(first_expense + second_expense)
    return pairs_sums


def prefix_three_sums(pairs_sums, report):
    pass


if __name__ == '__main__':
    print(first_solution())
