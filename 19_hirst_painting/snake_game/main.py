from snake import Snake
from food import Food
from turtle import Screen
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # Detect collision with food.
    if snake.head.distance(food) <15:
        print("collision happend..")
        food.refresh()
        score.increase_score()
        snake.extend_snake()

    # Detect collision with wall..
    if (snake.head.xcor() > 280 or snake.head.xcor() < -280 ) or (snake.head.ycor() > 280 or snake.head.ycor() < -280):
        is_game_on = False
        score.game_over()
        
    # Detetc collision with tell. (itself).
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            score.game_over()

screen.exitonclick()
