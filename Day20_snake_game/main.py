import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Charmer")
screen.tracer(0)  # hold off onscreen update until screen.update() below

# create snake using class Snake imported from paddles.py
snake = Snake()
food = Food()

# start listening for keystrokes to steer the snake
screen.listen()

screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
score_board = ScoreBoard()

game_on = True


while game_on:

    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()

    # Detect collision with walls
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_on = False
        score_board.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score_board.game_over()


screen.exitonclick()
