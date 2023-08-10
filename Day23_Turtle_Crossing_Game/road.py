from turtle import Turtle

END_X = 300
FIRST = (0, 250)
SECOND = (0, -250)


class Road:

    def __init__(self):
        self.makeLines()
        self.makeLane(FIRST)
        self.makeLane(SECOND)

    def makeLines(self):
        startX = -280
        while startX < END_X:
            line = Turtle()
            line.color("white")
            line.shape("square")
            line.shapesize(0.5, 1)
            line.penup()
            line.goto(startX, line.ycor())
            startX += 40

    def makeLane(self, location):
        lane = Turtle()
        lane.color("white")
        lane.shape("square")
        lane.shapesize(0.5, 30)
        lane.penup()
        lane.goto(location)
