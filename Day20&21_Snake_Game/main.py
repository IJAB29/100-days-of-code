from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.tracer(0)
screen.title("SNEK GEM")

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

speed = 0.1
gameOver = False
while not gameOver:

    """SNAKE EATS FOOD"""
    if snake.snakeHead.distance(food) < 15:
        food.relocate()
        scoreboard.increaseScore()
        scoreboard.updateHighScore()
        snake.extendSnakeSegments()

    """SNAKE HITS A WALL"""
    if snake.snakeHead.xcor() > 280 or snake.snakeHead.xcor() < -280 \
            or snake.snakeHead.ycor() > 280 or snake.snakeHead.ycor() < -280:
        scoreboard.gameOver()
        gameOver = True

    """SNAKE EATS IT'S OWN TAIL"""
    for seg in snake.snakeBody[1:]:
        if snake.snakeHead.distance(seg) < 10:
            scoreboard.gameOver()
            gameOver = True

    screen.update()
    time.sleep(speed)
    snake.move()

screen.exitonclick()
