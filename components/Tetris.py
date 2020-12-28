from components.Figure import Figure
from constants.GameStates import START, GAME_OVER


class Tetris:
    height = 0
    width = 0
    field = []
    score = 0
    state = START
    Figure = None

    def __init__(self, _height, _width):
        self.height = _height
        self.width = _width
        self.field = []
        self.score = 0
        self.state = START
        for i in range(_height):
            new_line = []
            for j in range(_width):
                new_line.append(0)
            self.field.append(new_line)
        self.new_figure()

    def new_figure(self):
        next_figure = Figure(3, 0)
        if self.intersects(next_figure):
            self.state = GAME_OVER
            return
        self.Figure = next_figure

    def go_down(self):
        self.Figure.y += 1
        if self.intersects():
            self.Figure.y -= 1
            self.freeze()

    def side(self, dx):
        old_x = self.Figure.x
        edge = False
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in self.Figure.image():
                    if (
                        j + self.Figure.x + dx > self.width - 1  # beyond right border
                        or j + self.Figure.x + dx < 0  # beyond left border
                    ):
                        edge = True
        if not edge:
            self.Figure.x += dx
        if self.intersects():
            self.Figure.x = old_x

    def left(self):
        self.side(-1)

    def right(self):
        self.side(1)

    def down(self):
        while not self.intersects():
            self.Figure.y += 1
        self.Figure.y -= 1
        self.freeze()

    def rotate(self):
        old_rotation = self.Figure.rotation
        self.Figure.rotate()
        if self.intersects():
            self.Figure.rotation = old_rotation

    def intersects(self, fig=None):
        fig = self.Figure if (fig is None) else fig
        intersection = False
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in fig.image():
                    if (
                        i + fig.y > self.height - 1  # bottom intersection
                        # or i + fig.y < 0  #
                        or self.field[i + fig.y][j + fig.x] > 0  # figure intersection
                    ):
                        intersection = True
        return intersection

    def freeze(self):
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in self.Figure.image():
                    self.field[i + self.Figure.y][j + self.Figure.x] = (
                        self.Figure.type + 1
                    )
        self.break_lines()
        self.new_figure()

    def break_lines(self):
        lines = 0
        for i in range(1, self.height):
            zeros = 0
            for j in range(self.width):
                if self.field[i][j] == 0:
                    zeros += 1
            if zeros == 0:
                lines += 1
                for i2 in range(i, 1, -1):
                    for j in range(self.width):
                        self.field[i2][j] = self.field[i2 - 1][j]
        self.score += lines ** 2
