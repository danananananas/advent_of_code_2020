def map_chars(seats, mapping):
    return seats.translate(str.maketrans(mapping))


def decode_numbering(code, coding):
    code = [int(bit)*power for bit, power in zip(code, coding)]
    return sum(code)


def decode_seat(seat_code, row_coding, col_coding):
    row = seat_code[:-3]
    column = seat_code[-3:]
    row = decode_numbering(row, row_coding)
    column = decode_numbering(column, col_coding)
    return row, column


def decode_seat_id(seat_code, row_coding, col_coding, mapping):
    seat = map_chars(seat_code, mapping)
    row, column = decode_seat(seat, row_coding, col_coding)
    return row * 8 + column


def get_seat_coding(length):
    return [2**n for n in range(length - 1, -1, -1)]


def decode_file(filename):
    mapping = {'F': '0', 'B': '1', 'L': '0', 'R': '1'}
    row_coding = get_seat_coding(7)
    col_coding = get_seat_coding(3)
    with open(filename) as f:
        seat_ids = [decode_seat_id(seat.strip(), row_coding, col_coding, mapping) for seat in f]
    return seat_ids


def solution_part_1(seat_ids):
    return max(seat_ids)


def partial_sum(k, n):
    if k > n:
        raise ValueError('n can not be less than k')
    return int(- (k - n - 1) * (k + n) / 2)


if __name__ == '__main__':
    input_seat_ids = decode_file('input.txt')
    print(solution_part_1(input_seat_ids))
