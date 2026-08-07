import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()

t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)
colors_list = ['firebrick', 'dark red', 'gold','indigo','deep pink','green yellow','lime','blue','alice blue','medium spring green','antique white','medium purple']

tim.speed('fastest')
def draw_circle_shape(size_shape):
    for x in range(int(360/size_shape)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+size_shape)

draw_circle_shape(5)

screen.exitonclick()