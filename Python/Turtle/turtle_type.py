'''Turtle_type.py by Dash McLaughlin
writes the phrase hello world
'''


import turtle
import math

size = 15                       # Sets font size
SANGLE = size * math.sqrt(3) + 10   # sets size for 30deg angles
LANGLE = size*2 * math.sqrt(2)  # sets size for 45deg angles

def write_H():
    '''writes an H'''
    turtle.down()
    turtle.forward(size*4)
    turtle.forward(-size*2)
    turtle.left(90)
    turtle.forward(size*2)
    turtle.right(90)
    turtle.forward(size*2)
    turtle.forward(-size*4)
    turtle.left(90)
    turtle.up()
    turtle.forward(size)
    turtle.right(90)

def write_E():
    '''writes an E'''
    turtle.down()
    turtle.forward(size*4)
    turtle.left(90)
    turtle.forward(size*2)
    turtle.left(90)
    turtle.up()
    turtle.forward(size*2)
    turtle.down()
    turtle.left(90)
    turtle.forward(size*2)
    turtle.right(90)
    turtle.forward(size*2)
    turtle.right(90)
    turtle.forward(size*2)
    turtle.up()
    turtle.forward(size)
    turtle.right(90)

def write_L():
    '''writes a L'''
    turtle.down()
    turtle.forward(size*4)
    turtle.left(90)
    turtle.forward(size*2)
    turtle.left(90)
    turtle.up()
    turtle.forward(size*4)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)

def write_O():
    '''writes an O'''
    turtle.down()
    turtle.forward(size*4)
    turtle.left(90)
    turtle.forward(size*2)
    turtle.left(90)
    turtle.forward(size*4)
    turtle.left(90)
    turtle.forward(size*2)
    turtle.up()
    turtle.forward(-size*3)
    turtle.left(90)

def write_W():
    '''writes a W'''
    turtle.down()
    turtle.forward(size*4)
    turtle.left(150)
    turtle.forward(SANGLE)
    turtle.right(120)
    turtle.forward(SANGLE)
    turtle.left(150)
    turtle.forward(size*4)
    turtle.right(90)
    turtle.up()
    turtle.forward(size)
    turtle.right(90)

def write_R():
    '''writes a R'''
    turtle.down()
    turtle.forward(size*4)
    turtle.left(90)
    turtle.up()
    turtle.forward(size*2)
    turtle.down()
    turtle.left(135)
    turtle.forward(LANGLE)
    turtle.right(135)
    turtle.forward(size*2)
    turtle.left(90)
    turtle.forward(size*2)
    turtle.left(90)
    turtle.forward(size*2)
    turtle.up()
    turtle.forward(-size*3)
    turtle.left(90)

def write_D():
    '''writes a D'''
    turtle.down()
    turtle.forward(size*4)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(60)
    turtle.forward(SANGLE)
    turtle.left(60)
    turtle.forward(SANGLE)
    turtle.left(60)
    turtle.forward(size)
    turtle.up()
    turtle.forward(-size*3)
    turtle.left(90)

def write_SPACE():
    '''writes a space'''
    turtle.left(90)
    turtle.forward(size*3)
    turtle.right(90)

def write_HelloWorld():
    '''writes the phrase HELLO WORLD'''
    write_H()
    write_E()
    write_L()
    write_L()
    write_O()
    write_SPACE()
    write_W()
    write_O()
    write_R()
    write_L()
    write_D()

turtle.up()
turtle.forward(-200)  # going to starting position on screen
turtle.right(90)
write_HelloWorld()

turtle.exitonclick()

