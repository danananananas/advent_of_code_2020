def map_chars(seats, mapping):
    return seats.translate(str.maketrans(mapping))


def decode_numbering(code, coding):
    code = [int(bit)*power for bit, power in zip(code, coding)]
    return sum(code)


def decode_seat_id(seat_code, row_coding, col_coding):
    pass
