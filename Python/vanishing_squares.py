'''vanishingsquares.py by Dash McLaughlin
draws nesting squares'''

from turtle import *

def draw_square(size):
    ''' Draws a square with a given side length'''
    up()
    forward(size/2)
    down()
    right(90)
    forward(size/2)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size/2)
    right(90)
    up()
    forward(size/2)
    right(180)

def draw_vanishing_squares(size, scale):
    '''draws vanishing squares at given starting size, and given shirnkage scale'''
    if size <= 1:
        return
    draw_square(size)
    draw_vanishing_squares(size * (100 - scale) / 100, scale) #draw again at percentage

def tests():
    draw_vanishing_squares(50, 50)
    input("press the any key")
    reset()
    draw_vanishing_squares(32, 20)
    input("press the any key")
    reset()
    draw_vanishing_squares(32, -50)
    input("press the any key")
    reset()


setworldcoordinates(-20, -20, 20, 20)
#tests()
draw_vanishing_squares(32, 50)

exitonclick()
