import tkinter as tk
from snake.gen import position, snakeloc


class GameWindow(tk.Tk):

    def __init__(self, title, conf, game_map, game=None, on_exit=None, keybindings=None):
        super().__init__()
        super().title(title)
        super().configure(background=conf.color_bg)
        if conf.show_info_panel:
            super().geometry("%dx%d" % (conf.window_width, conf.window_height))

        self._conf = conf
        self._map = game_map
        self._grid_width = conf.map_width / (game_map.num_rows - 2)
        self._grid_height = conf.map_height / (game_map.num_cols - 2)
        self._init_widgets()
        self._init_draw_params()

        if game is not None:
            self._game = game
            self._snake = game.snake

    def show(self, game_loop=None):
        def cb():
            if callable(game_loop):
                game_loop()
            self._update_contents()
            self.after(self._conf.interval_draw, cb)
        self.after(100, cb)
        self.mainloop()


    def _draw_bg(self):
        self._canvas.create_rectangle(0, 0, self._conf.map_width, self._conf.map_height,
                                      fill=self._conf.color_bg, outline='')

    def _draw_map_contents(self):
        for i in range(self._map.num_rows - 2):
            for j in range(self._map.num_cols - 2):
                self._draw_grid(j * self._grid_width, i * self._grid_height,
                                self._map.point(position(i + 1, j + 1)).type)

