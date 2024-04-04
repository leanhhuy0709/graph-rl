import pygame as pg
import random as rd
import time
import sys


class Color:
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)
    BLACK = (0, 0, 0)
    GRAY = (127, 127, 127)
    PURPLE = (127, 0, 127)
    ORANGE = (255, 127, 0)
    CYAN = (0, 255, 255)
    PINK = (255, 0, 255)
    BROWN = (127, 63, 0)
    LAVENDER = (200, 162, 200)
    TEAL = (0, 128, 128)
    GOLD = (255, 215, 0)
    SILVER = (192, 192, 192)
    INDIGO = (75, 0, 130)
    MAROON = (128, 0, 0)
    COLOR_LIST = []

    @staticmethod
    def initColor():
        Color.COLOR_LIST = [
            Color.RED,
            Color.GREEN,
            Color.BLUE,
            Color.WHITE,
            Color.YELLOW,
            Color.BLACK,
            Color.GRAY,
            Color.PURPLE,
            Color.ORANGE,
            Color.CYAN,
            Color.PINK,
            Color.BROWN,
            Color.LAVENDER,
            Color.TEAL,
            Color.GOLD,
            Color.SILVER,
            Color.INDIGO,
            Color.MAROON
        ]

        Color.COLOR_LIST.remove(Color.WHITE)
        Color.COLOR_LIST.remove(Color.BLACK)

    @staticmethod
    def get_random_color():
        return rd.choice(Color.COLOR_LIST)

    @staticmethod
    def get_color(index: int):
        if index >= len(Color.COLOR_LIST):
            index %= len(Color.COLOR_LIST)
        return Color.COLOR_LIST[index]


class Visualize:
    width = 0
    height = 0
    is_running = True
    is_pause = False
    color_list = []

    window = None
    font = None

    @staticmethod
    def init(width: int, height: int, caption: str, font_size: int):
        Visualize.width = width
        Visualize.height = height

        pg.init()
        Visualize.window = pg.display.set_mode((width, height))
        pg.display.set_caption(caption)
        pg.font.init()
        Visualize.font = pg.font.SysFont('Comic Sans MS', font_size)
        Visualize.smallFont = pg.font.SysFont(
            'Comic Sans MS', int(font_size / 2))
        Visualize.color_list = Visualize.color_gradient()

        Visualize.is_running = True

        Color.initColor()

    @staticmethod
    def before_update():
        Visualize.window.fill((35, 117, 179))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                Visualize.is_running = False
                pg.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    Visualize.is_pause = not Visualize.is_pause

    @staticmethod
    def after_update(delay=0):
        pg.display.flip()
        time.sleep(delay)

    @staticmethod
    def draw_rect(color: tuple[int, int, int], rect_config: tuple[float, float, float, float], origin=(0.5, 0.5)):
        x, y, w, h = rect_config
        x -= origin[0] * w
        y -= origin[1] * h
        rect_config = x, y, w, h
        pg.draw.rect(Visualize.window, color, rect_config)

    @staticmethod
    def draw_circle(color: tuple[int, int, int], position: tuple[float, float], r: float, origin=(0.5, 0.5)):
        x, y = position

        x -= (origin[0] - 0.5) * r
        y -= (origin[1] - 0.5) * r
        pg.draw.circle(Visualize.window, color, (x, y), r)

    @staticmethod
    def draw_line(color: tuple[int, int, int], point1: tuple[float, float], point2: tuple[float, float], thickness: int):
        pg.draw.line(Visualize.window, color, point1, point2, thickness)

    @staticmethod
    def color_gradient():
        res = []
        for x in [0, 127, 255]:
            for y in [0, 127, 255]:
                for z in [0, 127, 255]:
                    if x == 0 and y == 0 and z == 0:
                        continue
                    if x == 255 and y == 255 and z == 255:
                        continue
                    res.append((x, y, z))
        res.sort(key=lambda x: (x[0] == 255 or x[0] == 0) +
                 (x[1] == 255 or x[1] == 0) + (x[2] == 255 or x[2] == 0))
        return res

    @staticmethod
    def get_random_color():
        return rd.choice(Visualize.color_list)

    @staticmethod
    def get_color(index: int):
        return Visualize.color_list[index]

    @staticmethod
    def draw_text(content: str, x: int, y: int, color: tuple[int, int, int], isSmall=False):
        if isSmall:
            text = Visualize.smallFont.render(content, True, color)
        else:
            text = Visualize.font.render(content, True, color)
        Visualize.window.blit(text, (x, y))
        pass

    @staticmethod
    def draw_board(x, y, alignX, alignY, args2D):
        width = len(args2D[0]) * alignX + 20
        height = len(args2D) * alignY + 20
        Visualize.drawRect(Color.WHITE, (x, y, width, height), (0, 0))
        for i in range(len(args2D)):
            args = args2D[i]
            for j in range(len(args)):
                arg = args[j]
                Visualize.draw_text(arg, x + alignX * j,
                                    y + alignY * i, (0, 0, 0))


'''
How to use
from visualize import *
from config import *

Visualize.init(600, 600, "Traffic Manager", 10)

while True:
    Visualize.before_update()
    if not Visualize.is_running:
        break

    Visualize.draw_line((0, 0, 0), (100, 103), (409, 320), 10)

    Visualize.after_update()
'''
