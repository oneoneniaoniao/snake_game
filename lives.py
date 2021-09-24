from turtle import Turtle, Screen

# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("Orange3")
# screen.title("ヘビゲーム")

LIVES_NUMBER = 3
LIVES_POSITION = [(i, 285) for i in range(200, 290, 90 // LIVES_NUMBER)]
print(LIVES_POSITION)


class Lives():
    def __init__(self, LIVES_NUMBER):
        self.lives = []
        self.number = LIVES_NUMBER
        for i in range(LIVES_NUMBER):
            life = Turtle("circle")
            life.shapesize(stretch_len=0.4, stretch_wid=0.6)
            life.color("yellow")
            life.penup()
            life.setposition(LIVES_POSITION[i])
            self.lives.append(life)

    def minus(self):
        self.lives[self.number - 1].color("gray")
        self.number -= 1
#
#
# lives = Lives(LIVES_NUMBER)
#
# screen.exitonclick()
