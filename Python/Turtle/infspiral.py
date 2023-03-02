import turtle

def draw_spiral(n):
    if n==0:
        return
    turtle.forward(n)
    turtle.right(90)
    draw_spiral(n-1)

turtle.speed(0)
draw_spiral(200)
turtle.exitonclick()