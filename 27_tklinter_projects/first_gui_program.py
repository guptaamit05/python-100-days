import tkinter


window = tkinter.Tk()
window.title("My First Program")

# window size
window.minsize(width=600, height=600)

# Label
my_label = tkinter.Label(text="My First Label", font=('Arial', 14, 'italic'))
my_label.pack()
my_label['text'] = "New Text value"
# OR
# my_label.config(text="New Text using Config method")



# Button event on click:
def buttonClicked():
    my_label.config(text="User changed the text by clicking on button..")
    print(input.get())
    

#Button
button = tkinter.Button(bg="gray", text="my new button", command=buttonClicked, font=('Arial', 24, 'normal'))
button.pack()


#input text box 
input = tkinter.Entry(width=20)
input.pack()
input.focus()





# import turtle
# tk = turtle.Turtle()
# tk.write()


window.mainloop()