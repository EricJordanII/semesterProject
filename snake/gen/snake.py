import random
from collections import deque

from snake.gen.dicrections import Dicrections
from snake.gen.snakeloc import snakeloc
from snake.gen.position import position


class Snake:
    def __init__(self, game_map, init_direc=None, init_bodies=None, init_types=None):
        self._map = game_map
        self._init_direc = init_direc
        self._init_bodies = init_bodies
        self._init_types = init_types
        self.reset(False)

    def reset(self, reset_map=True):
        rand_init = False
        if self._init_direc is None:
            rand_init = True
            head_row = random.randrange(2, self._map.num_rows - 2)
            head_col = random.randrange(2, self._map.num_cols - 2)
            head = position(head_row, head_col)

            self._init_direc = random.choice([Dicrections.l, Dicrections.u, Dicrections.r, Dicrections.d])
            self._init_bodies = [head, head.adj(Dicrections.opposite(self._init_direc))]

            self._init_types = []
            if self._init_direc == Dicrections.l:
                self._init_types.append(snakeloc.lefthead)
            elif self._init_direc == Dicrections.u:
                self._init_types.append(snakeloc.uphead)
            elif self._init_direc == Dicrections.r:
                self._init_types.append(snakeloc.righthead)
            elif self._init_direc == Dicrections.d:
                self._init_types.append(snakeloc.downhead)
            if self._init_direc == Dicrections.l or self._init_direc == Dicrections.r:
                self._init_types.append(snakeloc.hori)
            elif self._init_direc == Dicrections.u or self._init_direc == Dicrections.d:
                self._init_types.append(snakeloc.verti)

        self._steps = 0
        self._dead = False
        self._direc = self._init_direc
        self._direc_next = Dicrections.n
        self._bodies = deque(self._init_bodies)

        if reset_map:
            self._map.reset()
        for i, pos in enumerate(self._init_bodies):
            self._map.point(pos).type = self._init_types[i]

        if rand_init:
            self._init_direc = self._init_bodies = self._init_types = None

    def copy(self):
        m_copy = self._map.copy()
        s_copy = Snake(m_copy, Dicrections.n, [], [])
        s_copy._steps = self._steps
        s_copy._dead = self._dead
        s_copy._direc = self._direc
        s_copy._direc_next = self._direc_next
        s_copy._bodies = deque(self._bodies)
        return s_copy, m_copy

    @property
    def map(self):
        return self._map

    @property
    def steps(self):
        return self._steps

    @property
    def dead(self):
        return self._dead

    @dead.setter
    def dead(self, val):
        self._dead = val

    @property
    def direc(self):
        return self._direc

    @property
    def direc_next(self):
        return self._direc_next

    @direc_next.setter
    def direc_next(self, val):
        self._direc_next = val

    @property
    def bodies(self):
        return self._bodies

    def len(self):
        return len(self._bodies)

    def head(self):
        if not self._bodies:
            return None
        return self._bodies[0]

    def tail(self):
        if not self._bodies:
            return None
        return self._bodies[-1]

    def move_path(self, path):
        for p in path:
            self.move(p)

    def move(self, new_direc=None):
        if new_direc is not None:
            self._direc_next = new_direc

        if self._dead or \
           self._direc_next == Dicrections.n or \
           self._map.is_full() or \
           self._direc_next == Dicrections.opposite(self._direc):
            return

        old_head_type, new_head_type = self._new_types()
        self._map.point(self.head()).type = old_head_type
        new_head = self.head().adj(self._direc_next)
        self._bodies.appendleft(new_head)

        if not self._map.is_safe(new_head):
            self._dead = True
        if self._map.point(new_head).type == snakeloc.food:
            self._map.rm_food()
        else:
            self._rm_tail()

        self._map.point(new_head).type = new_head_type
        self._direc = self._direc_next
        self._steps += 1

    def _rm_tail(self):
        self._map.point(self.tail()).type = snakeloc.clear
        self._bodies.pop()

    def _new_types(self):
        old_head_type, new_head_type = None, None
        # new_head_type
        if self._direc_next == Dicrections.l:
            new_head_type = snakeloc.lefthead
        elif self._direc_next == Dicrections.u:
            new_head_type = snakeloc.uphead
        elif self._direc_next == Dicrections.r:
            new_head_type = snakeloc.righthead
        elif self._direc_next == Dicrections.d:
            new_head_type = snakeloc.downhead
        if (self._direc == Dicrections.l and self._direc_next == Dicrections.l) or \
           (self._direc == Dicrections.r and self._direc_next == Dicrections.r):
            old_head_type = snakeloc.hori
        elif (self._direc == Dicrections.u and self._direc_next == Dicrections.u) or \
             (self._direc == Dicrections.d and self._direc_next == Dicrections.d):
            old_head_type = snakeloc.verti
        elif (self._direc == Dicrections.r and self._direc_next == Dicrections.u) or \
             (self._direc == Dicrections.d and self._direc_next == Dicrections.l):
            old_head_type = snakeloc.leftup
        elif (self._direc == Dicrections.l and self._direc_next == Dicrections.u) or \
             (self._direc == Dicrections.d and self._direc_next == Dicrections.r):
            old_head_type = snakeloc.upright
        elif (self._direc == Dicrections.l and self._direc_next == Dicrections.d) or \
             (self._direc == Dicrections.u and self._direc_next == Dicrections.r):
            old_head_type = snakeloc.rightdown
        elif (self._direc == Dicrections.r and self._direc_next == Dicrections.d) or \
             (self._direc == Dicrections.u and self._direc_next == Dicrections.l):
            old_head_type = snakeloc.downleft
        return old_head_type, new_head_type
