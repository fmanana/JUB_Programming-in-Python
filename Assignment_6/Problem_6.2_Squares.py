from turtle import Turtle

def drawSquares(t, length):
    t.pencolor('green')
    t.up()
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.down()
    for sides in range(4):
        for count in range(4):
            t.forward(length)
            t.left(90)
        t.forward(400)
        t.left(90)


t = Turtle()
t.screen.setup(width = 700, height = 700)
length = int(input())
drawSquares(t, length)
