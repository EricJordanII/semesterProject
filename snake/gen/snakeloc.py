from enum import Enum, unique

class snakeloc(Enum):
    clear = 0
    edge = 1
    food = 2
    lefthead = 100
    uphead = 101
    righthead = 102
    downhead = 103
    leftup = 104
    upright = 105
    rightdown = 106
    downleft = 107
    hori = 108
    verti = 109


class Point:
    def __init__(self):
        self._type = snakeloc.clear

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, val):
        self._type = val
