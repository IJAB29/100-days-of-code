from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
BOUNDARY = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.newLevel()

    def newLevel(self):
        self.goto(STARTING_POSITION)

    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def down(self):
        if self.ycor() > -BOUNDARY:
            self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)

