import random

from snake.gen.snakeloc import Point, snakeloc
from snake.gen.position import position


class Map:

    def __init__(self, num_rows, num_cols):
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._capacity = (num_rows - 2) * (num_cols - 2)
        self._content = [[Point() for _ in range(num_cols)] for _ in range(num_rows)]
        self.reset()

    def reset(self):
        self._food = None
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                if i == 0 or i == self._num_rows - 1 or \
                   j == 0 or j == self._num_cols - 1:
                    self._content[i][j].type = snakeloc.edge
                else:
                    self._content[i][j].type = snakeloc.clear

    def copy(self):
        m_copy = Map(self._num_rows, self._num_cols)
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                m_copy._content[i][j].type = self._content[i][j].type
        return m_copy

    @property
    def num_rows(self):
        return self._num_rows

    @property
    def num_cols(self):
        return self._num_cols

    @property
    def capacity(self):
        return self._capacity

    @property
    def food(self):
        return self._food

    def point(self, pos):
        return self._content[pos.x][pos.y]

    def is_inside(self, pos):
        return pos.x > 0 and pos.x < self.num_rows - 1 \
               and pos.y > 0 and pos.y < self.num_cols - 1

    def is_empty(self, pos):
        return self.is_inside(pos) and self.point(pos).type == snakeloc.clear

    def is_safe(self, pos):
        return self.is_inside(pos) and (self.point(pos).type == snakeloc.clear or \
                                        self.point(pos).type == snakeloc.food)

    def is_full(self):
        for i in range(1, self.num_rows - 1):
            for j in range(1, self.num_cols - 1):
                t = self._content[i][j].type
                if t.value < snakeloc.lefthead.value:
                    return False
        return True

    def has_food(self):
        return self._food is not None

    def rm_food(self):
        if self.has_food():
            self.point(self._food).type = snakeloc.clear
            self._food = None

    def create_food(self, pos):
        self.point(pos).type = snakeloc.food
        self._food = pos
        return self._food

    def create_rand_food(self):
        empty_pos = []
        for i in range(1, self._num_rows - 1):
            for j in range(1, self._num_cols - 1):
                t = self._content[i][j].type
                if t == snakeloc.clear:
                    empty_pos.append(position(i, j))
                elif t == snakeloc.food:
                    return None
        if empty_pos:
            return self.create_food(random.choice(empty_pos))
        else:
            return None
