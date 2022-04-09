from defines import RED, WHITE
from myengine import myengine
from myengine.display import Display
from myengine.keyboard import KeyboardEventsType, KeyboardEventsKey
from myengine.label import Label
from screen import Screen


class ScreenMenu(Screen):
    COLOR_NORMAL = WHITE
    COLOR_SELECT = RED
    FONT_SIZE = 60
    ITEMS = ("Start", "About", "Exit")

    def __init__(self):
        super().__init__()
        self.state = 0
        pass

    def draw(self, display):
        super().draw(display)

        for index, item in enumerate(self.ITEMS):
            if self.state == index:
                label = Label(item, font_color=self.COLOR_SELECT, font_size=self.FONT_SIZE)
            else:
                label = Label(item, font_color=self.COLOR_NORMAL, font_size=self.FONT_SIZE)

            width, height = label.get_size()

            w, h = display.get_size()

            x = (w / 2) - (width / 2)

            t_h = len(self.ITEMS) * height
            y = (h / 2) - (t_h / 2) + (index * height)

            display.set_label(label, x, y)

    def events_handler(self, event):
        if super().events_handler(event):
            return True
        elif event.type == KeyboardEventsType.KEYDOWN:
            if event.key == KeyboardEventsKey.K_UP:
                if self.state > 0:
                    self.state -= 1
                return True
            elif event.key == KeyboardEventsKey.K_DOWN:
                if self.state < len(self.ITEMS) - 1:
                    self.state += 1
                return True
            elif event.key == KeyboardEventsKey.K_RETURN:
                # print('enter')
                self.complete = True
                return True

        return False

    def proc(self):
        return self.complete, self.state
