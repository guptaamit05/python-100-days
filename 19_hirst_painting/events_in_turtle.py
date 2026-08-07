import turtle as t


tim = t.Turtle()
screen = t.Screen()


screen.listen()


def move_forward():
    tim.forward(10)

def move_backword():
    tim.backward(10)    
def move_counter_clockwise():
    tim.left(90)
def counter_clockwise():
    tim.right(90)
def clear_pad():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    
# screen.onkey(key="space", fun=move_forward )

screen.onkeypress(move_forward, "w")
screen.onkeypress(move_counter_clockwise, "s")
screen.onkeypress(counter_clockwise, "d")
screen.onkeypress(clear_pad, "c")

screen.exitonclick()





