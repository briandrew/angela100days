import turtle
from turtle import Turtle
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.make_snake()
        self.head = self.segments[0]

    def make_snake(self):

        block_x = 0
        for segment_index in range(0, 3):
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.goto(x=block_x, y=0)
            self.segments.append(new_segment)
            block_x -= 20

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def left(self):
        self.head.left(90)

    def right(self):
        self.head.right(90)





