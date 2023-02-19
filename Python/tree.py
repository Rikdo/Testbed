from turtle import *

def tree(n, s):
    if n<=0:
        return
    forward(s)
    left(45)
    tree(n-1, s/2)
    right(90)
    tree(n-1, s/2)
    left(45)
    forward(-s)

def test():
    tree(3,50)
    input()
    reset()
    tree(5,150)
    input()
    reset()
    left(90)
    speed(0)
    tree(10,150)
    input()
    reset()


left(90)
test()
#tree(3,100)
input()
