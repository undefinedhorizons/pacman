import pygame


class Clock:
    clock = None

    def __init__(self):
        self.clock = pygame.time.Clock()
        pass

    def tick(self, t):
        self.clock.tick(t)
