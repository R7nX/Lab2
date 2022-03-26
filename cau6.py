from turtle import *


for time in range(2):
    forward(100)
    left(90)
forward(150)
left(90)
forward(100)
left(90)
forward(50)

penup()
backward(50)
pendown()
left(90)

for logo in range(12):
    pencolor('#de5246')
    forward(100)
    right(130)
    forward(100)
    left(81)
    forward(98)
    right(131)
    forward(100)
    penup()
    right(90)
    forward(150)
    right(90)
    pendown()




mainloop()