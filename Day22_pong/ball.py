from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")

        self.goto(0, 0)

    def move(self):
        new_x = self.xcor() + 20
        new_y = self.ycor() + 10

        self.goto(new_x, new_y)




