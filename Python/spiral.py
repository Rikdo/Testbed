import turtle

def draw_spiral(width, size, max_size):
    '''Draws a spiral with given width, starting size, and maximum size
        (recursive)''' 
    if size >= max_size:
        return
    turtle.forward(size)
    turtle.right(90)
    draw_spiral(width, size + width, max_size)

WIDTH = 10          # set width, or tightness of spiral
START_SIZE = 10     # sets starting size of spiral
MAX_SIZE = 200      # sets ending length of spiral

draw_spiral(WIDTH, START_SIZE, MAX_SIZE)

turtle.exitonclick()
