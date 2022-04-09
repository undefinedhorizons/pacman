import pygame


class Label:
    def __init__(self, text, font_color=(0, 0, 0), font_ttf=None, font_size=25):
        self.font = pygame.font.Font(font_ttf, font_size)
        self.label = self.font.render(text, True, font_color)

    def get_size(self):
        return self.label.get_width(), self.label.get_height()


