import random

from defines import BLACK, WHITE, CELL_SIZE, BLUE
from levels import environment
from myengine.display import Display
from myengine.sprite import Sprite, spritecollide, rotateimage


class Player(Sprite):
    WIDTH = CELL_SIZE
    HEIGHT = CELL_SIZE
    SPEED = 3

    def __init__(self, x, y, walls):
        super().__init__(x=x * CELL_SIZE, y=y * CELL_SIZE, height=self.HEIGHT, width=self.WIDTH, filename="res/player.png")
        self.x = x * CELL_SIZE
        self.y = y * CELL_SIZE
        self.d_x = 0
        self.d_y = 0
        self.walls = walls
        self.image = self.sprite.image

    def update(self, *args, **kwargs):
        super().move(self.d_x, self.d_y)
        if len(spritecollide(self, self.walls, False)) > 0:
            # print(block)
            super().move(-self.d_x, -self.d_y)
            self.d_x = 0
            self.d_y = 0

    def move_right(self):
        self.d_x = self.SPEED
        self.d_y = 0
        self.sprite.image = rotateimage(self.sprite.image, 0)

    def move_left(self):
        self.d_x = -self.SPEED
        self.d_y = 0
        self.sprite.image = rotateimage(self.sprite.image, 180)

    def move_up(self):
        self.d_x = 0
        self.d_y = -self.SPEED
        self.sprite.image = rotateimage(self.sprite.image, 90)

    def move_down(self):
        self.d_x = 0
        self.d_y = self.SPEED
        self.sprite.image = rotateimage(self.sprite.image, 270)

    def start(self, key):
        self.sprite.image = self.image
        # antijump 2
        self.sprite.rect.topleft = (self.x, self.y)

    def stop(self):
        x, y = self.sprite.rect.topleft
        #print(x, y)
        mod_x = x % CELL_SIZE
        mod_y = y % CELL_SIZE
        if mod_x > 0:
            i = int(x/CELL_SIZE)
            if mod_x > CELL_SIZE/2:
                i = i + 1
            x = i * CELL_SIZE
        if mod_y > 0:
            j = int(y/CELL_SIZE)
            if mod_y > CELL_SIZE/2:
                j = j + 1
            y = j * CELL_SIZE
        #print(x, y)
        self.x = x
        self.y = y
        # antijump 1
        # self.sprite.rect.topleft = (self.x, self.y)
        self.d_x = 0
        self.d_y = 0