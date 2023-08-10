from turtle import Turtle


class Net:

    def __init__(self):
        yCoord = 290
        while yCoord > - 300:
            net = Turtle()
            net.color("white")
            net.penup()
            net.shape("square")
            net.shapesize(0.5, 0.2)
            net.goto(0, yCoord)
            yCoord -= 20
