#!/usr/bin/env python
# -*- coding: utf-8 -*-
from screen_about import ScreenAbout
from screen_level import ScreenLevel
from screen_menu import ScreenMenu


class ScreenFactory:
    @staticmethod
    def get(type_="ScreenMenu"): # by default
        screen = None
        if type_ == "ScreenMenu":
            screen = ScreenMenu()
        elif type_ == "ScreenAbout":
            screen = ScreenAbout()
        elif type_ == "ScreenLevel":
            screen = ScreenLevel()
        else:
            raise NotImplementedError()

        return screen

    @staticmethod
    def proc(screen):
        done = False
        class_name = screen.__class__.__name__
        complete, state = screen.proc()
        # print(screen.__class__.__name__, complete, state)
        if class_name == "ScreenMenu":
            if complete:
                if state == 0:
                    screen = ScreenLevel()
                elif state == 1:
                    screen = ScreenAbout()
                elif state == 2:
                    done = True

        if class_name == "ScreenAbout":
            if complete:
                screen = ScreenMenu()

        if class_name == "ScreenLevel":
            if complete:
                screen = ScreenMenu()

        return screen, done


