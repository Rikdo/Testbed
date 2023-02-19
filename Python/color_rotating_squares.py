from turtle import *

def draw_square(size):
    up()
    forward(size/2)
    right(90)
    down()
    forward(size/2)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size/2)
    up()
    right(90)
    forward(size/2)
    right(180)

def rotating_squares(size, max_itt, itt):
    if itt <= max_itt:
        if itt % 2 == 1:
            color('red')
        else:
            color('black')
        draw_square(size)
        right(360/max_itt)
        rotating_squares(size, max_itt, itt + 1)
        exitonclick()
    else:
        return

speed('fast')
rotating_squares(200, 50, 0)
exitonclick()
