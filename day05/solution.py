def map_chars(seats, mapping):
    return seats.translate(str.maketrans(mapping))


def decode_seat(seat_code):
    row = seat_code[:-3]
    column = seat_code[-3:]
    row = int(row, 2)
    column = int(column, 2)
    return row, column


def decode_seat_id(seat_code, mapping):
    seat = map_chars(seat_code, mapping)
    row, column = decode_seat(seat)
    return row * 8 + column


def decode_file(filename):
    mapping = {'F': '0', 'B': '1', 'L': '0', 'R': '1'}
    with open(filename) as f:
        seat_ids = [decode_seat_id(seat.strip(), mapping) for seat in f]
    return seat_ids


def solution_part_1(seat_ids):
    return max(seat_ids)


def partial_sum(k, n):
    if k > n:
        raise ValueError('n can not be less than k')
    return int(- (k - n - 1) * (k + n) / 2)


def solution_part_2(seat_ids):
    all_seats_summed = partial_sum(min(seat_ids), max(seat_ids))
    taken_seats_summed = sum(seat_ids)
    return all_seats_summed - taken_seats_summed


if __name__ == '__main__':
    input_seat_ids = decode_file('input.txt')
    print(solution_part_1(input_seat_ids))
    print(solution_part_2(input_seat_ids))
