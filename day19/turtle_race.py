
from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Pick turtle to win - enter a color: ")
print(user_bet)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_start = 105
is_race_on = False
all_turtles = []

# make 6 turtles that line up on start line
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_start - 30)
    all_turtles.append(new_turtle)
    y_start -= 30

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 225:
            is_race_on = False  # to stop turtles
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win! The {winning_color} turtle is the winner.")
            else:
                print(f"You lost! The {winning_color} turtle won")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
