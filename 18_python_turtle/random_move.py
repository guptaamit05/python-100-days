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

random_move = [0, 90,180,270 ]
colors_list = ['firebrick', 'dark red', 'gold','indigo','deep pink','green yellow','lime','blue','alice blue','medium spring green','antique white','medium purple']

tim.pensize(15)
tim.speed('fastest')
for _ in range(100):
    # tim.color(random.choice(colors_list))
    tim.pencolor(random_color())
    tim.forward(30)
    tim.setheading(random.choice(random_move))


screen.exitonclick()