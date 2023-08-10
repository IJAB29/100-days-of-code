from turtle import Screen
from pong import Pong
from net import Net
from scoreboard import ScoreBoard
from ball import Ball
import time


screen = Screen()
screen.bgcolor("black")
screen.title("PONG GAEM")
screen.setup(width=800, height=600)
screen.tracer(0)

player1 = Pong((360, 0))
player2 = Pong((-360, 0))
net = Net()
ball = Ball()
player1Score = ScoreBoard(1)
player2Score = ScoreBoard(2)

screen.listen()
screen.onkeypress(fun=player1.up, key="Up")
screen.onkeypress(fun=player1.down, key="Down")
screen.onkeypress(player2.up, "w")
screen.onkeypress(player2.down, "s")


screen.update()


inPlay = True
while inPlay:
    if ball.ycor() > 260 or ball.ycor() < -260:
        ball.wallBounce()

    if player1.distance(ball) < 80 and ball.xcor() > 320 or player2.distance(ball) < 80 and ball.xcor() < -320:
        ball.pongBounce()

    if ball.xcor() > 360:
        player2Score.increaseScore()
        ball.serve(player2)
    elif ball.xcor() < -360:
        player1Score.increaseScore()
        ball.serve(player1)

    ball.move()
    screen.update()
    time.sleep(ball.ballSpeed)
    # player2.compMove()

screen.exitonclick()
