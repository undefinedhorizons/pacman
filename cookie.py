from defines import BLACK, WHITE, CELL_SIZE
from myengine.display import Display
from myengine.sprite import Sprite


class Cookie(Sprite):
    WIDTH = 8
    HEIGHT = 8
    COLOR = WHITE

    def __init__(self, x, y):
        super().__init__(x=x * CELL_SIZE + 12, y=y * CELL_SIZE + 12, height=self.HEIGHT, width=self.WIDTH, color=BLACK)

        Display.set_ellipse(self.sprite.image, self.COLOR, [0, 0, self.WIDTH, self.HEIGHT])
