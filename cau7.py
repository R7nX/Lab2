from tkinter import Y
from turtle import *

pencolor('#cf8f03')

x = 100
y = 5

for one in range(y):
    x = x + 1
    left(25)
    forward(x)
    right(50)
    forward(x)
    right(130)
    forward(x)
    right(50)
    forward(x)
    left(205)

penup()
forward(90)
pendown()
pencolor('#0b2c3c')

for one in range(y):
    left(25)
    forward(x)
    right(50)
    forward(x)
    right(130)
    forward(x)
    right(50)
    forward(x)
    left(205)


mainloop()
