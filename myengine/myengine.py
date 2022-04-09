import pygame


class MyEngine:
    sprite = None

    def __init__(self):
        pass

    @staticmethod
    def init():
        pygame.init()

    @staticmethod
    def quit():
        pygame.quit()
