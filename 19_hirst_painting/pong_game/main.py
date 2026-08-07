from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from sccoreboard import Scoreboard



screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_up, 'Up')
screen.onkey(r_paddle.move_down, 'Down')

screen.onkey(l_paddle.move_up, 'w')
screen.onkey(l_paddle.move_down, 's')


is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    # Detect top bottom ball collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # Detect collision with right|left paddle.
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or (ball.distance(l_paddle)<50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect R paddle misses.
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
    
    # Detect L paddle misses.
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
