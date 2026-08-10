import turtle as t
import pandas

image = "./blank_states_img.gif"
screen = t.Screen()

screen.title("Find State of US")
screen.addshape(image)
t.shape(image)

# Read the csv and try to find the name of state that user typed..
data = pandas.read_csv("./50_states.csv")
states = data.state.to_list()

#input model..
guess_states = []
while len(guess_states) < 10:
    answer_state = screen.textinput(title=f"{len(guess_states)}/50 States Correct", prompt="Enter the state name")
    if answer_state == None:
        break
    
    answer_state = answer_state.title()
    if answer_state == 'Exit':
        break

    if answer_state in states:
        # print("Exist")
        guess_states.append(answer_state)
        tt = t.Turtle()
        tt.hideturtle()
        tt.penup()
        state_data = data[data.state == answer_state]
        tt.goto(state_data.x.item(), state_data.y.item())
        tt.write(state_data.state.item())
    else:
        print("Wrong input..")


# screen.exitonclick()