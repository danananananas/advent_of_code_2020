def decode_row(row):
    pass


def map_chars(seats):
    mapping = {'F': '0', 'B': '1', 'L': '0', 'R': '1'}
    return seats.translate(str.maketrans(mapping))
