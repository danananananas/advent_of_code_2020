from helper import read_input_w_double_return, read_input_w_double_n_single_return


def count_unique_group_answers(group):
    return len(set(group))


def count_all_unique_group_answers(filename):
    group_answers = read_input_w_double_return(filename)
    return [count_unique_group_answers(group) for group in group_answers]


def count_only_answered_by_all_groups(group):
    intersected = set(group[0])
    for person in group[1:]:
        intersected = intersected & set(person)
    return len(intersected)


def count_all_only_answered_by_all_groups(filename):
    group_answers = read_input_w_double_n_single_return(filename)
    return [count_only_answered_by_all_groups(group) for group in group_answers]


def solution_1():
    return sum(count_all_unique_group_answers('input.txt'))


def solution_2():
    return sum(count_all_only_answered_by_all_groups('input.txt'))


if __name__ == '__main__':
    print(solution_1())
    print(solution_2())
