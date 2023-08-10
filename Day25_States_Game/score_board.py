from turtle import Turtle

FONT = ("Courier", 20, "normal")
ALIGNMENT = "center"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(160, 220)
        self.hideturtle()
        # self.showScore()

    def showScore(self):
        self.clear()
        self.write(f"Correct Guesses: {self.score}/50", align=ALIGNMENT, font=FONT)

    def increaseScore(self):
        self.score += 1
        # self.showScore()

    def youWin(self):
        self.goto(0, 0)
        self.write("YOU WIN!", align=ALIGNMENT, font=FONT)
