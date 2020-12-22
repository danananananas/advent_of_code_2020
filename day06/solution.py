from helper import read_input_w_double_n_single_return


def count_unique_group_answers(group):
    in_any_answer = set().union(*(set(person) for person in group))
    return len(in_any_answer)


def count_all_unique_group_answers(group_answers):
    return sum((count_unique_group_answers(group) for group in group_answers))


def count_only_answered_by_all_groups(group_answers):
    in_all_answer = set(group_answers[0])
    in_all_answer = in_all_answer.intersection(*(set(person_answers) for person_answers in group_answers))
    return len(in_all_answer)


def count_all_only_answered_by_all_groups(group_answers):
    return sum((count_only_answered_by_all_groups(group) for group in group_answers))


if __name__ == '__main__':
    answers = read_input_w_double_n_single_return('input.txt')
    print(count_all_unique_group_answers(answers))
    print(count_all_only_answered_by_all_groups(answers))
