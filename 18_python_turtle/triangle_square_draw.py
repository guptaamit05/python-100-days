from turtle import Turtle, Screen
import random
colors = ['red', 'black', 'green', 'orange', 'yellow', 'gray']
tim = Turtle()
screen = Screen()

tim.speed(3)
tim.shape("turtle")
# tim.color("red")

def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        tim.right(angle)
        tim.forward(100)
        

for n in range(3,8):
    col = random.choice(colors)
    tim.color(col)
    draw_shape(n)
    
    
screen.exitonclick()