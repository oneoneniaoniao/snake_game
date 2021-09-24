from turtle import Turtle, Screen
import time

screen = Screen()
screen.tracer(0)

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
EYES_STARTING_POSITION = [(-3, 0), (3, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self, difficulty):
        self.segments = []
        self.eyes = []
        self.create_snake()
        self.head = self.segments[0]
        self.move_distance = difficulty

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
        for i in range(2):
            eye = Turtle(shape="circle")
            eye.penup()
            eye.color("black")
            eye.shapesize(stretch_len=0.15, stretch_wid=0.2)
            eye.setposition(EYES_STARTING_POSITION[i])
            self.eyes.append(eye)

    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.penup()
        segment.setposition(position)
        segment.color("green")
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].setposition(self.segments[i - 1].position())
        self.head.forward(self.move_distance)
        self.eyes[0].forward(self.move_distance)
        self.eyes[1].forward(self.move_distance)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.eyes[0].setheading(UP)
            self.eyes[1].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.eyes[0].setheading(DOWN)
            self.eyes[1].setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.eyes[0].setheading(RIGHT)
            self.eyes[1].setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.eyes[0].setheading(LEFT)
            self.eyes[1].setheading(LEFT)

    def collide(self):
        for i in self.segments[1:]:
            if self.head.distance(i) <= 5:
                return True

    def dead(self):
        for i in range(2):
            self.eyes[i].color("white")

    def eye_close(self):
        time.sleep(0.1)
        for i in self.eyes:
            i.shapesize(stretch_len=0.15, stretch_wid=0.08)
        screen.update()

    def eye_open(self):
        time.sleep(0.1)
        for i in self.eyes:
            i.shapesize(stretch_len=0.15, stretch_wid=0.2)
        screen.update()

    def restart(self):
        snake_len = len(self.segments)
        for i in self.segments:
            i.setposition(1000, 1000)
        for i in self.eyes:
            i.setposition(1000, 1000)
        self.segments.clear()
        self.eyes.clear()
        self.create_snake()
        self.head = self.segments[0]
        for i in range(snake_len - 3):
            self.extend()
        #
        # self.head.setposition(-600, 0)
        # self.head.setheading(0)
        # self.eyes[0].setposition(-600 - 3, 0)
        # self.eyes[0].color("black")
        # self.eyes[0].setheading(0)
        # self.eyes[1].setposition(-600 + 3, 0)
        # self.eyes[1].color("black")
        # self.eyes[1].setheading(0)