'''
square.py by Dash McLaughlin
draws squares
'''

import turtle

def draw_square(size):
    ''' Draws a square with a given side length'''
    turtle.up()
    turtle.forward(size/2)
    turtle.down()
    turtle.right(90)
    turtle.forward(size/2)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size/2)
    turtle.right(90)
    turtle.up()
    turtle.forward(size/2)
    turtle.right(180)

def draw_two_squares(size, angle):
    '''draws two squares at given size, at given angle degree angle'''
    draw_square(size) #Draw first square 
    turtle.right(angle) #Change angle to draw second square
    draw_square(size) #Draw second square

def test():
    draw_two_squares(-200, 45)
    draw_two_squares(200, -30)
    draw_two_squares(100, 45)
    draw_two_squares(200, 30)

# draw_two_squares(200, 45)
test()
turtle.exitonclick()
