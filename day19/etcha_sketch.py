import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
turtle.colormode(255)


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def clockwise():
    tim.right(5.0)


def counter_clockwise():
    tim.left(5.0)


def reset_turtle():
    turtle.resetscreen()


screen.listen()
# screen.onkey(key="w", fun=move_forward)  # move_forward when space bar pressed
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="d", fun=clockwise)
# screen.onkey(key="a", fun=counter_clockwise)
# screen.onkey(key="c", fun=reset_turtle)
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="d", fun=clockwise)
screen.onkeypress(key="a", fun=counter_clockwise)
screen.onkey(key="c", fun=reset_turtle)


screen.exitonclick()
