import colorgram
import turtle
from random import choice

turtle.colormode(255)
turtle.speed("fastest")
screen = turtle.Screen()
animal = turtle.Turtle()
animal.hideturtle()

# colors = colorgram.extract("image.jpg", 30)
# rgbVals = []
#
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     rgbVals.append((r, g, b))


def setStartPos(x, y):
    animal.penup()
    animal.goto(x, y)


def drawDots(length, width):
    for y in range(length):
        for x in range(width):
            animal.dot(20, choice(rgbColors))
            animal.forward(50)
        animal.setx(animal.xcor() - 50 * width)
        animal.sety(animal.ycor() + 50)


rgbColors = [(211, 154, 98), (53, 107, 131), (177, 78, 33), (198, 142, 35), (116, 155, 171), (124, 79, 98), (123, 175, 157), (226, 197, 130), (190, 88, 109), (12, 50, 64), (56, 39, 19), (41, 168, 128), (50, 126, 121), (199, 123, 143), (166, 21, 30), (224, 93, 79), (243, 163, 161), (38, 32, 34), (3, 25, 25), (80, 147, 169), (161, 26, 22), (21, 78, 90), (234, 167, 171), (171, 206, 190), (103, 127, 156), (165, 202, 210)]

setStartPos(-250, -250)
drawDots(10, 10)
screen.exitonclick()
