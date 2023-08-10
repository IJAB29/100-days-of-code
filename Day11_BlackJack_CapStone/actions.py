from turtle import Turtle, Screen
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.tracer(0)
screen.title("SNEK GEM")

score = 3
snakeBody = []
snakeHead = Turtle("square")
snakeHead.color("white")
snakeHead.penup()
snakeBody.append(snakeHead)

for i in range(score - 1):
    snakePart = Turtle("square")
    snakePart.color("white")
    snakePart.penup()
    snakePart.setx(snakeHead.xcor() - 20)
    snakeBody.append(snakePart)


speed = (score - 2) / 10
gameOver = False
while not gameOver:
    screen.update()
    time.sleep(speed)
    for segmentNum in range(len(snakeBody)-1, -1, -1):
        if segmentNum == 0:
            snakeBody[segmentNum].forward(20)
        else:
            snakeBody[segmentNum].goto(snakeBody[segmentNum - 1].xcor(), snakeBody[segmentNum - 1].ycor())
        if snakeBody[segmentNum].xcor() < -580 and snakeBody[segmentNum].xcor() > 580 and snakeBody[segmentNum].ycor() < -580 and snakeBody[segmentNum].ycor() > 580:
            gameOver = True
            
screen.exitonclick()