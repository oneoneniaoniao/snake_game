from turtle import Turtle, Screen
import time

screen = Screen()
screen.tracer(0)


class Heart:
    def __init__(self, x, y):
        self.seg = []
        square = Turtle("square")
        square.penup()
        square.setheading(45)
        square.color("red")
        square.setposition(x, y)
        self.seg.append(square)
        circle_l = Turtle("circle")
        circle_l.penup()
        circle_l.shapesize(1)
        circle_l.color("red")
        circle_l.setposition(x - 8, y + 8)
        self.seg.append(circle_l)
        circle_r = Turtle("circle")
        circle_r.penup()
        circle_r.shapesize(1)
        circle_r.color("red")
        circle_r.setposition(x + 8, y + 8)
        self.seg.append(circle_r)
        screen.update()

    def show_heart(self):
        time.sleep(0.1)
        for i in self.seg:
            i.showturtle()
        screen.update()

    def hide_heart(self):
        time.sleep(0.1)
        for i in self.seg:
            i.hideturtle()
        screen.update()

    def heart_blinks(self):
        for i in range(3):
            self.show_heart()
            self.hide_heart()

# screen = Screen()
# heart = Heart(10, 10)
# heart.heart_blinks()
#
# screen.exitonclick()
