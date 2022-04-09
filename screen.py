from defines import RED
from myengine.keyboard import KeyboardEventsType, KeyboardEventsKey
from myengine.label import Label


class Screen:
    complete = None

    def __init__(self):
        self.complete = False
        pass

    def draw(self, display):
        pass

    def events_handler(self, event):
        if event.type == KeyboardEventsType.KEYDOWN:
            if event.key == KeyboardEventsKey.K_ESCAPE:
                print('esc')
                self.complete = True
                return True

        return False

    def proc(self):
        return self.complete
