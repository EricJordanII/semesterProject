import sys
import random
from collections import deque
from snake.gen import Dicrections, snakeloc
from snake.solving.base import BaseSolver


class _TableCell:

    def __init__(self):
        self.reset()

    def __str__(self):
        return "{ dist: %d  parent: %s  visit: %d }" % \
               (self.dist, str(self.parent), self.visit)
    __repr__ = __str__

    def reset(self):
        self.parent = None
        self.dist = sys.maxsize
        self.visit = False


class PathSolver(BaseSolver):

    def __init__(self, snake):
        super().__init__(snake)
        self._table = [[_TableCell() for _ in range(snake.map.num_cols)]
                       for _ in range(snake.map.num_rows)]

    @property
    def table(self):
        return self._table



    def longest_path_to(self, des):
        path = self.shortest_path_to(des)
        if not path:
            return deque()

        self._reset_table()
        cur = head = self.snake.head()

        return path

    def _reset_table(self):
        for row in self._table:
            for col in row:
                col.reset()

    def _build_path(self, src, des):
        path = deque()
        tmp = des
        while tmp != src:
            parent = self._table[tmp.x][tmp.y].parent
            path.appendleft(parent.direc_to(tmp))
            tmp = parent
        return path

    def _is_valid(self, pos):
        return self.map.is_safe(pos) and not self._table[pos.x][pos.y].visit
