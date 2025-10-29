import time
from turtle import Screen
from snake import Snake
from snake_Food import Food
from scoreboard import Scoreboard

scoreboard = Scoreboard()
with open("data.txt",mode="r") as data:
    highscore = int(data.read())
scores = [highscore]
while True:

    scoreboard.high_score = max(scores)
    with open("data.txt",mode="w") as data:
        data.write(f"{scoreboard.high_score}")

    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snakuu Gamee!")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    food.hideturtle()
    scoreboard.score = 0

    scoreboard.display_high_score()

    screen.listen()
    screen.onkey(fun=snake.right,key="Right")
    screen.onkey(fun=snake.left,key="Left")
    screen.onkey(fun=snake.up, key="Up")
    screen.onkey(fun=snake.down, key="Down")

    game_on = True
    while game_on:
        scoreboard.score_update()
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) < 15:
            food.clear()
            food = Food()
            snake.extend()
            scoreboard.increase_score()
            scores.append(scoreboard.score)
            scoreboard.display_high_score()

        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            game_on = False
            scoreboard.display_high_score()

        for part in snake.snake_body[1:]:
            if snake.head.distance(part) < 10:
                game_on = False
                scoreboard.display_high_score()

    screen.clear()



screen.exitonclick()
