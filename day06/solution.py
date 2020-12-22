from helper import read_input_w_double_return


def count_unique_group_answers(group):
    return len(set(group))


def count_all_unique_group_answers(filename):
    group_answers = read_input_w_double_return(filename)
    return [count_unique_group_answers(group) for group in group_answers]


def solution_1():
    return sum(count_all_unique_group_answers('input.txt'))


if __name__ == '__main__':
    print(solution_1())
