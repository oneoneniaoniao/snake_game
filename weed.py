from turtle import Turtle, Screen
from random import randint


# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("Orange3")
# screen.title("ヘビゲーム")

def make_weed():
    weed = Turtle()
    weed.hideturtle()
    weed.penup()
    weed.pencolor("green")
    weed.pensize(3)
    x = randint(-300, 300)
    y = randint(-300, 300)
    weed.setposition(x, y)
    weed.pendown()
    weed.goto(x - 2, y + 9)
    weed.penup()
    weed.goto(x + 4, y)
    weed.pendown()
    weed.goto(x + 4, y + 7)
    weed.penup()
    weed.goto(x + 8, y)
    weed.pendown()
    weed.goto(x + 8, y + 9)
    weed.penup()
    weed.goto(x + 12, y)
    weed.pendown()
    weed.goto(x + 13, y + 10)
    weed.penup()
    weed.goto(x + 15, y)
    weed.pendown()
    weed.goto(x + 17, y + 6)
    weed.penup()


def weeds(n):
    for i in range(n):
        make_weed()

# screen = Screen()
#
# screen.exitonclick()
