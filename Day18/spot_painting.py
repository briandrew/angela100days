# import colorgram - only needed to use once
import turtle
from turtle import Turtle, Screen
from random import choice

# only needed to run once to get the rgb's out of the image

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# create tuple of just rgb codes in order to delete out those close to white
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g, b)
#     rgb_colors.append(new_color)


# this is the original copy of the print(rgb_colors):
'''[(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136),
 (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
 (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171),
 (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
 (176, 192, 208), (168, 99, 102)]'''
# this is the copy with the white-ish ones removed so they show up
color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136),
 (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
 (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171),
 (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
 (176, 192, 208), (168, 99, 102)]


tim = Turtle()
tim.shape('turtle')
tim.hideturtle()
tim.color('white')
turtle.colormode(255)  # so can use RGB for pencolor below
tim.pensize(10)
tim.speed('fast')
# need initial location to be upper left corner
current_location = tim.pos()
print(current_location)

for j in range(10):
    for i in range(10):
        tim.dot(20, choice(color_list))
        tim.penup() # stays up until gets to tim.dot again
        tim.forward(50)

    current_location = tim.pos()
    tim.setx(current_location[0] - 500)
    tim.sety(current_location[1] + 40)

    tim.pendown()


# make_spots(2)

screen = Screen()
screen.exitonclick()


