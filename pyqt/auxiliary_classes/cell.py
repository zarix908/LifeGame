import math


def is_int(value):
    try:
        return math.modf(value)[1] == value
    except Exception:
        return False


class Cell:
    def __init__(self, x, y):
        if not (is_int(x) and is_int(y)):
            raise TypeError("arguments should be integer type")

        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def copy(self):
        return Cell(self.x, self.y)
