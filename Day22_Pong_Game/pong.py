from turtle import Turtle

PONG_SPEED = 20
UP = 90
DOWN = 270
Y_BOUNDARY = 240


class Pong(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(1, 5)
        self.setheading(UP)
        # self.pongSpeed = 20
        self.goto(position)

    def up(self):
        # self.pongSpeed = 20
        self.setheading(UP)
        if Y_BOUNDARY > self.ycor():
            self.move()

    def down(self):
        # self.pongSpeed = -20
        self.setheading(DOWN)
        if self.ycor() > -Y_BOUNDARY:
            self.move()

    def move(self):
        # self.sety(self.ycor() + self.pongSpeed)
        self.forward(PONG_SPEED)

    def compMove(self):
        self.move()
        if self.ycor() > Y_BOUNDARY:
            self.down()
        elif self.ycor() < -Y_BOUNDARY:
            self.up()
