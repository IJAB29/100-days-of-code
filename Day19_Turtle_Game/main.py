from turtle import Turtle, Screen
import turtle as pokemon
from random import randint

screen = Screen()
pokemon.speed("fastest")

# screen.listen()
# turtle.shape("turtle")
# turtle.color("green")
#
#
# def moveForward():
#     turtle.forward(10)
#
#
# def moveBackward():
#     turtle.back(10)
#
#
# def turnCounterClockwise():
#     turtle.left(10)
#
#
# def turnClockwise():
#     turtle.right(10)
#
#
# screen.onkeypress(key= "w", fun= moveForward)
# screen.onkeypress(key= "s", fun= moveBackward)
# screen.onkeypress(key= "a", fun= turnCounterClockwise)
# screen.onkeypress(key= "d", fun= turnClockwise)
# screen.onkeypress(key= "c", fun= turtle.reset)


def setStartPos(x, y, animal):
    animal.penup()
    animal.goto(x, y)


def winner():
    raceStart = True

    while raceStart:
        for turt in turtles:
            if turt.xcor() > 230:
                raceStart = False
                return turt.pencolor()

            turt.forward(randint(1, 10))


screen.setup(height=400, width=500)
bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")
turtleColors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtles = []

y = -150
for i in turtleColors:
    turtle = Turtle("turtle")
    turtle.color(i)
    setStartPos(-230, y, turtle)
    turtles.append(turtle)
    y += 50

if bet:
    if winner() == bet:
        print("You win!")
    else:
        print("You lose.")


screen.exitonclick()