from enum import Enum, unique


class Dicrections(Enum):
    n = 0
    l = 1
    u = 2
    r = 3
    d = 4

    def opposite(d):
        if d == Dicrections.l:
            return Dicrections.r
        elif d == Dicrections.r:
            return Dicrections.l
        elif d == Dicrections.u:
            return Dicrections.d
        elif d == Dicrections.d:
            return Dicrections.u
        else:
            return Dicrections.n
