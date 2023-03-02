from turtle import *

def drawCircles(n, size):
    if n <= 0:
        return
    down()
    circle(size)
    up()
    
    forward(size)
    left(90)
    forward(size)
    right(90)
    down()
    drawCircles(n-1, size/2)
    up()
    forward(-size)
    down()
    drawCircles(n-1, size/2)
    

recursion = 3
Size = 100
#speed(0)
drawCircles(recursion, Size)
exitonclick()
