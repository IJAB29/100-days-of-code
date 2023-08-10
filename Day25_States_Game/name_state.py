from turtle import Turtle

FONT = ("Courier", 8, "normal")
ALIGNMENT = "center"


class NameState(Turtle):

    def __init__(self, name, xLoc, yLoc):
        super().__init__()
        self.penup()
        self.goto(xLoc, yLoc)
        self.hideturtle()
        self.write(name, align=ALIGNMENT, font=FONT)
