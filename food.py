from turtle import Turtle
from random import randint

RANGE = 260
FOOD_SIZE = 0.5


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("black")
        self.shapesize(FOOD_SIZE)
        self.setposition(randint(-RANGE, RANGE), randint(-RANGE, RANGE))

    def new_position(self):
        self.setposition(randint(-RANGE, RANGE), randint(-RANGE, RANGE))
        self.showturtle()
