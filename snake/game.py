import errno
import os
import traceback
from enum import Enum, unique

from snake.gen import Dicrections, Map, snakeloc, position, Snake
from snake.gui import GameWindow
from snake.solving import HamiltonSolver

@unique
class GameMode(Enum):
    n = 0


class setup:
    def __init__(self):
        self.mode = GameMode.n
        self.solver_name = 'HamiltonSolver'
        self.map_rows = 20
        self.map_cols = self.map_rows
        self.map_width = 800
        self.map_height = self.map_width
        self.info_panel_width = 155
        self.window_width = self.map_width
        self.window_height = self.map_height
        self.grid_pad_ratio = 0.25
        self.show_grid_line = False
        self.show_info_panel = False
        self.interval_draw = 50
        self.interval_draw_max = 200

        self.color_bg = '#2251b1'
        self.color_txt = '#F5F5F5'
        self.color_wall = '#F5F5F5'
        self.color_food = '#ee2236'
        self.color_head = '#c7c7c7'
        self.color_body = '#F5F5F5'

        self.init_direc = Dicrections.r
        self.init_bodies = [position(1, 4), position(1, 3), position(1, 2), position(1, 1)]
        self.init_types = [snakeloc.righthead] + [snakeloc.hori] * 3


class Game:

    def __init__(self, conf):
        self._conf = conf
        self._map = Map(conf.map_rows + 2, conf.map_cols + 2)
        self._snake = Snake(self._map, conf.init_direc,
                            conf.init_bodies, conf.init_types)
        self._pause = False
        self._solver = globals()[self._conf.solver_name](self._snake)
        self._episode = 1

    @property
    def snake(self):
        return self._snake

    @property
    def episode(self):
        return self._episode

    def run(self):
        window = GameWindow("Snake", self._conf, self._map, self, self._on_exit)
        if self._conf.mode == GameMode.n:
            window.show(self._game_main_normal)

