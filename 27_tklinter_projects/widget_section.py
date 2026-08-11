import tkinter



window = tkinter.Tk()
window.title("Widget Examples")
window.minsize(width=600, height=600)

# adding padding to window
window.config(padx=10, pady=5)

#Label
label = tkinter.Label(text="My New Label")
label.grid(column=0,row=0)


# Get Input Text box value:
def getText():
    print("Value of Text: ", input.get())

#Input box
input = tkinter.Entry(width=30 )
input.grid(column=1, row=0)


#Button
button = tkinter.Button(width=20, command=getText, text="Click button")
# button.pack()  ################# Either use pack or grid but not both....
button.config()
button.grid(column=1, row=2, padx=10, pady=10)  ## work with cordinate..



# Multiline text box..
textarea = tkinter.Text(height=5, width=20)
textarea.grid(column=1, row=3)





window.mainloop()




