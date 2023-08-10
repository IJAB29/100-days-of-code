from turtle import Turtle

FONT = ("Aerial", 24, "bold")
HIGH_SCORE_FONT = ("Aerial", 15, "normal")
ALIGNMENT = "center"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.showScore()
        self.highScore = Turtle()
        self.highScore.color("white")
        self.highScore.hideturtle()
        self.highScore.penup()
        self.highScore.goto(220, 265)
        with open("high_score.txt") as file:
            self.highestScore = file.read()
        self.showHighScore()

    def showScore(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def showHighScore(self):
        self.highScore.clear()
        self.highScore.write(f"High Score: {self.highestScore}", font=HIGH_SCORE_FONT, align=ALIGNMENT)

    def updateHighScore(self):
        if self.score > int(self.highestScore):
            with open("high_score.txt", "w") as file:
                file.write(str(self.score))
        self.showHighScore()

    def increaseScore(self):
        self.score += 1
        self.showScore()

    def gameOver(self):
        self.goto(0, 0)
        self.updateHighScore()
        self.write("Game Over.", align=ALIGNMENT, font=FONT)
