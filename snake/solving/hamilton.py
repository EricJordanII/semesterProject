from snake.gen import Dicrections
from snake.solving.base import BaseSolver
from snake.solving.path import PathSolver


class ham:

    def __init__(self):
        self.reset()

    def __str__(self):
        return "{ idx: %d  direc: %s }" % \
               (self.idx, self.direc)
    __repr__ = __str__

    def reset(self):
        self.idx = None
        self.direc = Dicrections.n


class HamiltonSolver(BaseSolver):

    def __init__(self, snake, shortcuts=True):
        super().__init__(snake)

        self._shortcuts = shortcuts
        self._path_solver = PathSolver(snake)
        self._table = [[ham() for _ in range(snake.map.num_cols)]
                        for _ in range(snake.map.num_rows)]
        self._build_cycle()
