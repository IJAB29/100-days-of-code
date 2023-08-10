from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10
STARTING_POSITIONS = [(320, -220), (320, 220), (320, 180), (320, 140), (320, 100), (320, -180), (320, -140),
                      (320, -100), (320, 60), (320, -60), (320, -20), (320, 20)]


class Cars:

    def __init__(self):
        super().__init__()
        self.moveSpeed = 5
        self.allCars = []

    def createCar(self):
        if random.randint(1, 4) == 1:
            car = Turtle()
            car.penup()
            car.goto(random.choice(STARTING_POSITIONS))
            car.color(random.choice(COLORS))
            car.shape("square")
            car.shapesize(1, 2)
            self.allCars.append(car)

    def move(self):
        for car in self.allCars:
            car.goto(car.xcor() - self.moveSpeed, car.ycor())

    def increaseCarSpeed(self):
        self.moveSpeed += MOVE_INCREMENT
