from turtle import Turtle, Screen

turtle_obj = Turtle() 
second_turtle = Turtle()

# second_turtle.setpos(40, 60)
second_turtle.teleport(20, 30)


turtle_obj.shape("turtle")
turtle_obj.color("green")

second_turtle.shape("turtle")
second_turtle.color("red")
turtle_obj.speed(1)
second_turtle.speed(1)

for _ in range(5):
    second_turtle.forward(10)
    second_turtle.penup()
    second_turtle.forward(10)
    second_turtle.pendown()
    
    
# for _ in range(4):
#     print("speed", turtle_obj.speed())
#     turtle_obj.forward(90)
#     turtle_obj.right(90)




screen = Screen()
screen.exitonclick()
