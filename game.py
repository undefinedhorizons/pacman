#!/usr/bin/env python
# -*- coding: utf-8 -*-
from defines import *
from screen_about import ScreenAbout
from screen_factory import ScreenFactory
from screen_menu import ScreenMenu
from screen_level import ScreenLevel
from myengine.clock import Clock
from myengine.display import Display
from myengine.keyboard import Keyboard, KeyboardEventsType


class Game:
    @staticmethod
    def run():
        clock = Clock()

        Display.set_mode(SCREEN_WIDTH, SCREEN_HEIGHT)
        Display.set_caption('PACMAN')

        done = False

        screen = ScreenFactory().get()
        # screen = ScreenFactory().get("ScreenAbout")
        # screen = ScreenFactory().get("ScreenLevel")

        # main loop
        while not done:
            # process
            screen, done = ScreenFactory().proc(screen)

            # events processing
            events = Keyboard.dispatch()
            for event in events:
                # print(event.type, KeyboardEventsType.QUIT)
                if event.type == KeyboardEventsType.QUIT:
                    done = True
                else:
                    screen.events_handler(event)

            # display screen
            Display.clear()
            screen.draw(Display)
            Display.render()

            # waiting next frame
            # print('tick')
            clock.tick(CLOCK_TICK)  # (1)
