import time
from turtle import Screen
from food import Food, FOOD_SIZE
from heart import Heart
from scoreboard import Scoreboard
from snake import Snake
from weed import weeds
from lives import Lives, LIVES_NUMBER

SLEEP_TIME = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("peru")
screen.title("ヘビゲーム")
screen.tracer(0)
weeds(20)
scoreboard = Scoreboard(0)
lives = Lives(LIVES_NUMBER)

difficulty = int(screen.textinput("むずかしさをえらんでね。", "やさしい：10、ふつう：15、むずかしい：20"))
snake = Snake(difficulty)
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(SLEEP_TIME)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) <= 30 * FOOD_SIZE:
        food.hideturtle()
        scoreboard.increase_score()
        heart = Heart(snake.head.xcor(), snake.head.ycor() + 40)
        food.new_position()
        for i in range(3):
            heart.show_heart()
            snake.eye_close()
            heart.hide_heart()
            snake.eye_open()
        snake.extend()

    # Detect collision with wall.
    if snake.head.xcor() < -280 or snake.head.xcor() > 275 or snake.head.ycor() < -270 or snake.head.ycor() > 280:
        lives.minus()
        snake.dead()
        screen.update()
        time.sleep(1)
        if lives.number == -1:
            scoreboard.game_over()
            screen.update()
            game_is_on = False
        else:
            snake.restart()
            screen.update()
            time.sleep(1)

    # Detect collision with tail.
    if snake.collide():
        lives.minus()
        snake.dead()
        screen.update()
        time.sleep(1)
        if lives.number == -1:
            scoreboard.game_over()
            screen.update()
            game_is_on = False
        else:
            snake.restart()
            screen.update()
            time.sleep(1)

screen.exitonclick()
