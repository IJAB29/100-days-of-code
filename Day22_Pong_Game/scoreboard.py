from turtle import Turtle

FONT = ("Comic Sans MS", 80, "bold")
ALIGNMENT = "center"


class ScoreBoard(Turtle):

    def __init__(self, player):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        if player == 1:
            self.goto(70, 170)
        else:
            self.goto(-70, 170)
        self.showScore()

    def showScore(self):
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def increaseScore(self):
        self.score += 1
        self.clear()
        self.showScore()

