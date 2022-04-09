from cookie import Cookie
from defines import RED, CELL_SIZE, BLUE, GREEN
from ghost import Ghost
from myengine.keyboard import KeyboardEventsType, KeyboardEventsKey
from myengine.label import Label
from levels import environment
from myengine.sprite import Group, spritecollide
from player import Player
from screen import Screen
from wall import Wall


class ScreenLevel(Screen):
    def __init__(self):
        super().__init__()

        self.walls = Group()
        self.cookies = Group()
        self.ghosts = Group()

        for i, row in enumerate(environment()):
            for j, item in enumerate(row):
                if item != 0:
                    self.walls.add(Wall(j, i, item))
                else:
                    self.cookies.add(Cookie(j, i))

        self.ghosts.add(Ghost(1, 3, 0, -2))
        self.ghosts.add(Ghost(22, 2, 2, 0))

        self.player = Player(9, 10, self.walls);

        self.score = 0

    def draw(self, display):
        super().draw(display)

        display.set_group(self.walls)
        display.set_group(self.cookies)
        display.set_group(self.ghosts)

        display.set_sprite(self.player);

        label = Label("Score: " + str(self.score), font_color=GREEN, font_size=35)
        display.set_label(label, 20, 20)

        self.ghosts.update()
        self.player.update()

        if len(spritecollide(self.player, self.cookies, True)) > 0:
            self.score += 1

        if len(spritecollide(self.player, self.ghosts, True)) > 0:
            # TODO:
            self.complete = True

    def events_handler(self, event):
        if super().events_handler(event):
            return True
        elif event.type == KeyboardEventsType.KEYDOWN:
            self.player.start(event.key);
            if event.key == KeyboardEventsKey.K_LEFT:
                self.player.move_left()
                return True
            elif event.key == KeyboardEventsKey.K_RIGHT:
                self.player.move_right()
                return True
            elif event.key == KeyboardEventsKey.K_UP:
                self.player.move_up()
                return True
            elif event.key == KeyboardEventsKey.K_DOWN:
                self.player.move_down()
                return True
            #elif event.key == KeyboardEventsKey.K_RETURN:
            #   print('enter')
            #   return True
        elif event.type == KeyboardEventsType.KEYUP:
            self.player.stop()
            return True
        return False

    def proc(self):
        return self.complete, self.score
