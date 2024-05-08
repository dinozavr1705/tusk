import tkinter as ttk
from tkinter import *
from math import pi


class Shape:
    def S(self):
        pass
class Circle(Shape):
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    @property
    def S(self):
        return pi * self.r * self.r

    def draw(self):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)

class Rect(Shape):
    def __init__(self,a,h):
        self.__a = a
        self.__h = h
    def S(self):
        return self.__a * self.__h * 0.5

room = Tk()
canvas = Canvas(width=2000, height=2000, bg='white')
canvas.pack()

circle1 = Circle(700, 350, 50)
circle2 = Circle(800, 350, 10)

circle1.draw()
circle2.draw()

room.mainloop()
