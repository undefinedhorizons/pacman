from defines import BLACK, WHITE, CELL_SIZE, BLUE
from myengine.display import Display
from myengine.sprite import Sprite


class Wall(Sprite):
    WIDTH = CELL_SIZE
    HEIGHT = CELL_SIZE
    COLOR = (0, 0, 16)  # BLACK
    BORDER_COLOR = BLUE
    BORDER_WIDTH = 3

    def __init__(self, x, y, mask=8):
        super().__init__(x=x * CELL_SIZE, y=y * CELL_SIZE, height=self.HEIGHT, width=self.WIDTH, color=self.COLOR)

        if mask & 1:  # left
            Display.set_line(self.sprite.image, self.BORDER_COLOR, [0, 0], [0, CELL_SIZE], self.BORDER_WIDTH)
        if mask & 2:  # top
            Display.set_line(self.sprite.image, self.BORDER_COLOR, [0, 0], [CELL_SIZE - 1, 0], self.BORDER_WIDTH)
        if mask & 4:  # right
            Display.set_line(self.sprite.image, self.BORDER_COLOR, [CELL_SIZE - 1, 0], [CELL_SIZE - 1, CELL_SIZE],
                             self.BORDER_WIDTH)
        if mask & 8:  # bottom
            Display.set_line(self.sprite.image, self.BORDER_COLOR, [0, CELL_SIZE], [CELL_SIZE - 1, CELL_SIZE], self.BORDER_WIDTH)
