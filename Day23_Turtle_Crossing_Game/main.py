import time
from turtle import Screen
from player import Player
from road import Road
from cars import Cars
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Crossing New Horizons")
screen.setup(600, 600)
screen.tracer(0)
screen.listen()
screen.bgcolor("black")

road = Road()
player = Player()
scoreboard = Scoreboard()
car = Cars()

screen.onkeypress(fun=player.up, key="Up")
screen.onkeypress(player.down, "Down")

delay = 0.1
isPlaying = True
allCars = []
while isPlaying:

    screen.update()
    time.sleep(delay)

    for i in car.allCars:
        if i.distance(player) < 30:
            isPlaying = False
            scoreboard.gameOver()

    if player.ycor() > 280:
        player.newLevel()
        car.increaseCarSpeed()
        scoreboard.increaseScore()

    car.createCar()
    car.move()

screen.exitonclick()
