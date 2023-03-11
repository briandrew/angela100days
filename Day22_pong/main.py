import time
from turtle import Screen, Turtle
from paddles import Paddle
from ball import Ball
from scoreboard import ScoreBoard

# setup screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=1800, height=1000)
screen.title("Pong")
screen.tracer(0)  # hold off onscreen updates (animations turned off) until screen.update() below

# create snake using class Snake imported from paddles.py


# paddle_right = Paddle()
ball = Ball()

r_paddle = Paddle((850, 0))
l_paddle = Paddle((-850, 0))

# start listening for keystrokes to steer the snake

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")


score_board = ScoreBoard()
ball.goto(0, 0)
game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()  # turns animations back on
    ball.move()

    # Detect paddle collision with ball
    if ball.distance(r_paddle) < 50 and ball.xcor() > 830 or ball.distance(l_paddle) < 50 and ball.xcor() < -830:
        ball.bounce_x()

    # Detect ball collision with top and bottom walls - top wall y=500, bottom wall y=-500
    if ball.ycor() > 480 or ball.ycor() < -480:
        ball.bounce_y()

    # detect when r_paddle misses
    if ball.xcor() > 880:
        ball.reset_position()
        score_board.l_point()

    # detect when l_paddle misses
    if ball.xcor() < -880:
        ball.reset_position()
        score_board.r_point()


    #     game_on = False
    #     score_board.game_over()
    #



screen.exitonclick()
