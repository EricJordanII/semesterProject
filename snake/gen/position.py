from snake.gen.dicrections import Dicrections


class position:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def __str__(self):
        return 'Pos(%d,%d)' % (self._x, self._y)
    __repr__ = __str__

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self._x == other.x and self._y == other.y
        return NotImplemented

    def __pos__(self):
        return position(self._x, self._y)

    def __neg__(self):
        return position(-self._x, -self._y)

    def __add__(self, other):
        if isinstance(self, other.__class__):
            return position(self._x + other.x, self._y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(self, other.__class__):
            return self + (-other)
        return NotImplemented

    def __hash__(self):
        return hash((self.x, self.y))

    @staticmethod
    def manhattan_dist(p1, p2):
        return abs(p1.x - p2.x) + abs(p1.y - p2.y)

    def direc_to(self, adj_pos):
        if self._x == adj_pos.x:
            diff = self._y - adj_pos.y
            if diff == 1:
                return Dicrections.l
            elif diff == -1:
                return Dicrections.r
        elif self._y == adj_pos.y:
            diff = self._x - adj_pos.x
            if diff == 1:
                return Dicrections.u
            elif diff == -1:
                return Dicrections.d
        return Dicrections.n

    def adj(self, direc):
        if direc == Dicrections.l:
            return position(self._x, self._y - 1)
        elif direc == Dicrections.r:
            return position(self._x, self._y + 1)
        elif direc == Dicrections.u:
            return position(self._x - 1, self._y)
        elif direc == Dicrections.d:
            return position(self._x + 1, self._y)
        else:
            return None

    def all_adj(self):
        adjs = []
        for direc in Dicrections:
            if direc != Dicrections.n:
                adjs.append(self.adj(direc))
        return adjs

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, val):
        self._x = val

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, val):
        self._y = val
