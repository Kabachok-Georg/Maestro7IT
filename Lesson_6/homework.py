from turtle import *
import random


class Block(Turtle):

    def __init__(self, size):
        self.size = size
        Turtle.__init__(self, shape="square", visible=False)
        self.pu()
        self.shapesize(size * 1.5, 1.5, 2)
        self.fillcolor("lightblue")  # Меняем цвет на светло-синий
        self.st()

    def glow(self):
        self.fillcolor("pink")

    def unglow(self):
        self.fillcolor("grey")

    def __repr__(self):
        return "Block size: {0}".format(self.size)


class Shelf(list):

    def __init__(self, y):
        self.y = y
        self.x = 0  # Начнем с центра

    def push(self, d):
        width, _, _ = d.shapesize()
        y_offset = width / 2 * 20
        d.sety(self.y + y_offset)
        d.setx(self.x + (len(self) - 1) * 34)  # Центрируем
        self.append(d)

    def _close_gap_from_i(self, i):
        for b in self[i:]:
            xpos, _ = b.pos()
            b.setx(xpos - 34)

    def _open_gap_from_i(self, i):
        for b in self[i:]:
            xpos, _ = b.pos()
            b.setx(xpos + 34)

    def pop(self, key):
        b = list.pop(self, key)
        b.glow()
        b.sety(200)
        self._close_gap_from_i(key)
        return b

    def insert(self, key, b):
        self._open_gap_from_i(key)
        list.insert(self, key, b)
        b.setx(self.x + key * 34)  # Центрируем
        width, _, _ = b.shapesize()
        y_offset = width / 2 * 20
        b.sety(self.y + y_offset)
        b.unglow()
