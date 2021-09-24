
from turtle import Turtle, Screen


ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):

    def __init__(self,a):
        super().__init__()
        with open("high_score") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.hideturtle()
        self.penup()
        self.setposition(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"スコア：{self.score}  ハイスコア：{self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,70)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        self.goto(0, 30)
        self.write(f"スコアは{self.score}てんだよ", align=ALIGNMENT, font=FONT)
        if self.high_score < self.score:
            self.high_score = self.score
            self.goto(0,-10)
            self.write("おめでとう！ハイスコアだよ！", align=ALIGNMENT, font=FONT)
            with open("high_score", mode="w") as file:
                file.write(f"{self.score}")

    def game_reset(self):
        self.score = 0
        self.hideturtle()
        self.penup()
        self.setposition(0, 270)
        self.update_scoreboard()


# screen = Screen()
# scoreboard = Scoreboard(3)
#
# screen.exitonclick()
