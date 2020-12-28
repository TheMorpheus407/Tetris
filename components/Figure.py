import random
from constants.Colors import brick_colors


class Figure:
    x = 0
    y = 0

    """
    Figure-matrix:

    0   1   2   3
    4   5   6   7
    8   9   10  11
    12  13  14  15
    """

    Figures = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],  # Gerade
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],  # Rev L
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],  # L
        [[1, 2, 5, 6]],  # BLOCK
        [[6, 7, 9, 10], [1, 5, 6, 10]],  # S
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],  # T
        [[4, 5, 9, 10], [2, 6, 5, 9]],  # Reverse S
    ]

    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord
        self.type = random.randint(0, len(self.Figures) - 1)
        self.color = brick_colors[self.type + 1]
        self.rotation = 0

    def image(self):
        return self.Figures[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.Figures[self.type])