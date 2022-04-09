import pygame
from enum import Enum


class KeyboardEventsType:
    QUIT = pygame.QUIT
    KEYDOWN = pygame.KEYDOWN
    KEYUP = pygame.KEYUP
    MOUSEBUTTONDOWN = pygame.MOUSEBUTTONDOWN


class KeyboardEventsKey:
    K_ESCAPE = pygame.K_ESCAPE
    K_RETURN = pygame.K_RETURN
    K_RIGHT = pygame.K_RIGHT
    K_LEFT = pygame.K_LEFT
    K_UP = pygame.K_UP
    K_DOWN = pygame.K_DOWN


class KeyboardEvent:
    type = None
    key = None

    def __init__(self):
        pass


class Keyboard:
    def __init__(self):
        pass

    @staticmethod
    def dispatch():
        r = []

        for event in pygame.event.get():
            ev = KeyboardEvent()
            ev.type = event.type
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                ev.key = event.key
            r.append(ev)

        return r
