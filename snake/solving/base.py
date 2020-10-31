
class BaseSolver:
    def __init__(self, snake):
        self._snake = snake
        self._map = snake.map

    @property
    def map(self):
        return self._map

    @property
    def snake(self):
        return self._snake

    @snake.setter
    def snake(self, val):
        self._snake = val
        self._map = val.map

