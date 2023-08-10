from turtle import Turtle

DISTANCE_BETWEEN_SEGMENTS = 20
MOVEMENT_SPEED = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
INITIAL_SEGMENTS = 3


class Snake:

    def __init__(self):
        self.snakeBody = []
        self.initialSnakeSegments()
        self.snakeHead = self.snakeBody[0]

    def initialSnakeSegments(self):
        """MAKE SNAKE INITIAL SEGMENTS"""
        startX = 0
        for i in range(INITIAL_SEGMENTS):
            self.addSnakeSegments((startX, 0))
            startX -= DISTANCE_BETWEEN_SEGMENTS

    def addSnakeSegments(self, position):
        snakeSegment = Turtle("square")
        snakeSegment.color("white")
        snakeSegment.penup()
        snakeSegment.goto(position)
        self.snakeBody.append(snakeSegment)

    def extendSnakeSegments(self):
        self.addSnakeSegments(self.snakeBody[-1].position())

    def move(self):
        for segmentNum in range(len(self.snakeBody) - 1, 0, -1):
            self.snakeBody[segmentNum].goto(self.snakeBody[segmentNum - 1].xcor(),
                                            self.snakeBody[segmentNum - 1].ycor())
        self.snakeHead.forward(MOVEMENT_SPEED)

    def up(self):
        if self.snakeHead.heading() != DOWN:
            self.snakeHead.setheading(UP)

    def down(self):
        if self.snakeHead.heading() != UP:
            self.snakeHead.setheading(DOWN)

    def left(self):
        if self.snakeHead.heading() != RIGHT:
            self.snakeHead.setheading(LEFT)

    def right(self):
        if self.snakeHead.heading() != LEFT:
            self.snakeHead.setheading(RIGHT)

