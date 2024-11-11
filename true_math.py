from math import inf


def divide(first, second):
    if second == 0:
        return inf
    else:
        rest = first / second
        return rest