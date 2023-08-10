from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x = 10
        self.y = 10
        self.ballSpeed = 0.1

    def serve(self, player):
        self.ballSpeed = 0.1
        if player.xcor() == 360:
            self.goto(player.xcor() - 40, player.ycor())
            self.x *= -1
        else:
            self.goto(player.xcor() + 40, player.ycor())

    def move(self):
        self.goto(self.xcor() + self.x, self.ycor() + self.y)

    def wallBounce(self):
        self.y *= -1

    def pongBounce(self):
        self.x *= -1
        self.ballSpeed *= 0.9

