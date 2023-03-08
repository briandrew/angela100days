
import turtle
from turtle import Turtle, Screen
from random import randint, choice

tim = Turtle()
tim.shape('turtle')
tim.color('pink')
turtle.colormode(255)  # so can use RGB for pencolor below
# tim.pensize(10)
tim.speed('fastest')


# def shape(sides_in):
#     for _ in range(sides_in):
#         tim.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
#         turn_angle = 360 / sides_in
#         tim.forward(100)
#         tim.right(turn_angle)

# heading = [0, 90, 180, 270]


# def random_walk(number_in):
#     for i in range(number_in):
#         tim.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
#         tim.setheading(choice(heading))
#         print(tim.heading())
#         tim.forward(100)

def spirograph():
    for i in range(36):
        tim.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
        tim.circle(100)
        tim.right(10)

        print(tim.heading())


# for i in range(3, 5):
#     shape(i)

# random_walk(50)
spirograph()

screen = Screen()
print(tim.heading())
screen.exitonclick()
