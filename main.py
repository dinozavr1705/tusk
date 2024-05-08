import tkinter as ttk
from tkinter import *
from math import pi


class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    @property
    def S(self):
        return pi * self.r * self.r

    def draw(self):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)


room = Tk()
canvas = Canvas(width=2000, height=2000, bg='white')
canvas.pack()

circle1 = Circle(700, 350, 50)
circle2 = Circle(800, 350, 10)

circle1.draw()
circle2.draw()

room.mainloop()
