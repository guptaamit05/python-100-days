import colorgram
import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()
t.colormode(255)
# colors = colorgram.extract("./hirst_spots.jpg", 9)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b    
#     rgb_colors.append((r,g,b))

# print(rgb_colors)    

color_list = [(253, 251, 247), (253, 248, 252), (235, 252, 243), (198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5)]

tim.penup()
tim.hideturtle()
tim.speed('fastest')
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
for dot_count in range(1, 101):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen.exitonclick()




