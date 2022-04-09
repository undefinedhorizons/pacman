from defines import RED
from myengine.keyboard import KeyboardEventsType, KeyboardEventsKey
from myengine.label import Label
from screen import Screen


class ScreenAbout(Screen):
    def __init__(self):
        super().__init__()

    def draw(self, display):
        super().draw(display)

        label = Label("It is an arcade Game", font_color=RED, font_size=35)

        width, height = label.get_size()

        w, h = display.get_size()

        x = (w / 2) - (width / 2)
        y = (h / 2) - (height / 2)

        display.set_label(label, x, y)

    def events_handler(self, event):
        if super().events_handler(event):
            return True
        elif event.type == KeyboardEventsType.KEYDOWN:
            if event.key == KeyboardEventsKey.K_RETURN:
                # print('enter')
                self.complete = True
                return True
        return False

    def proc(self):
        return self.complete, None
