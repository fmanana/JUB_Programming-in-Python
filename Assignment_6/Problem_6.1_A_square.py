from turtle import Turtle

def drawSquare(t, length):
    t.up()
    t.forward(length/2)
    t.left(90)
    t.forward(length/2)
    t.left(90)
    t.down()
    for sides in range(4):
        t.forward(length)
        t.left(90)
    t.up

t = Turtle()
t.screen.setup(width = 600, height = 600)

length = int(input("Enter an integer: "))
drawSquare(t, length)