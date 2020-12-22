def map_chars(seats, mapping):
    return seats.translate(str.maketrans(mapping))


def decode_numbering(code, coding):
    code = [int(bit)*power for bit, power in zip(code, coding)]
    return sum(code)
