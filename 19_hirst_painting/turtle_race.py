import turtle as t
import random


screen = t.Screen()
screen.setup(width=600, height=500)
user_input = screen.textinput(title="Turtle's Race", prompt="Which color's turtle will win the race?")
colors = ['red', 'green', 'blue', 'orange', 'black', 'yellow']
y_position = [-120, -80,-40, 0, 40, 80]
is_race_on = False
all_turtle = []
for turtle_index in range(len(colors)):
    
    tim = t.Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(x=-280, y=y_position[turtle_index])
    all_turtle.append(tim)


if user_input:
    is_race_on = True


while is_race_on:
    
    for each_turtle in all_turtle:
        if each_turtle.xcor() >=280:
            is_race_on = False
            winning_turtle_color = each_turtle.pencolor()
            if winning_turtle_color == user_input:
                print(f"You'r  {user_input} turtle is won")
            else:
                print(f"Your have lost. The Winner color: {winning_turtle_color} is the winner.")
        rand_dist = random.randint(0,10)
        each_turtle.forward(rand_dist)

screen.exitonclick()