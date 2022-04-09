#!/usr/bin/env python
# -*- coding: utf-8 -*-
from myengine.myengine import MyEngine
from game import Game


def main():
    MyEngine.init()

    Game.run()

    MyEngine.quit()


if __name__ == '__main__':
    main()
