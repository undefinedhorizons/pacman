import random

from defines import BLACK, WHITE, CELL_SIZE, BLUE
from levels import environment
from myengine.display import Display
from myengine.sprite import Sprite


class Ghost(Sprite):
    WIDTH = CELL_SIZE
    HEIGHT = CELL_SIZE

    def __init__(self, x, y, d_x, d_y):
        super().__init__(x=x * CELL_SIZE, y=y * CELL_SIZE, height=self.HEIGHT, width=self.WIDTH, filename="res/ghost.png")
        self.d_x = d_x
        self.d_y = d_y

    def update(self, *args, **kwargs):
        # print('update')
        super().move(self.d_x, self.d_y)

        x, y = super().get_rect().topleft
        if x % CELL_SIZE == 0 and y % CELL_SIZE == 0:
            level = environment()
            i = int(x / CELL_SIZE)
            j = int(y / CELL_SIZE)

            if i >= 0 and j >= 0 and level[j][i] == 0:
                choice = tuple()

                # print(j, i, level[j][i - 1], level[j][i + 1], level[j - 1][i], level[j + 1][i], )

                if level[j][i - 1] == 0:
                    choice = choice + ("left",)
                if level[j][i + 1] == 0:
                    choice = choice + ("right",)
                if level[j - 1][i] == 0:
                    choice = choice + ("up",)
                if level[j + 1][i] == 0:
                    choice = choice + ("down",)

                if choice != ("left", "right") and choice != ("up", "down"):
                    # print(choice)

                    direction = random.choice(choice)

                    # print(direction)

                    if direction == "left":  # and self.d_x == 0:
                        self.d_x = -2
                        self.d_y = 0
                    elif direction == "right":  # and self.d_x == 0:
                        self.d_x = 2
                        self.d_y = 0
                    elif direction == "up":  # and self.d_y == 0:
                        self.d_x = 0
                        self.d_y = -2
                    elif direction == "down":  # and self.d_y == 0:
                        self.d_x = 0
                        self.d_y = 2
