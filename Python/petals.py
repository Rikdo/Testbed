import turtle

def draw_square(size):#Draws Square from center, at side length "size"
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

def draw_awsome(angle, size):
    if size <= -200:
        return
    turtle.right(angle)
    draw_square(size)
    draw_awsome(angle, size-10)

turtle.speed(0)
draw_awsome(5, 200)
turtle.exitonclick()
