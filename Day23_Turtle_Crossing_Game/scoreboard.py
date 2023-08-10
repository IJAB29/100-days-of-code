from turtle import Turtle

FONT = ("Courier", 24, "bold")
ALIGNMENT = "center"
POSITION = (-290, 260)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(POSITION)
        self.score = 0
        self.showScore()

    def showScore(self):
        self.write(f"Score: {self.score}", font=FONT)

    def increaseScore(self):
        self.score += 1
        self.clear()
        self.showScore()

    def gameOver(self):
        self.goto(0, 0)
        self.write("GAME OVER",align=ALIGNMENT, font=FONT)
