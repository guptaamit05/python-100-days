import tkinter


window = tkinter.Tk()

window.title("Miles to Km Converter")
window.minsize(width=300, height=100)


def miles_to_km():
    miles_value = float(miles_text.get())
    km_value = round(miles_value * 1.689, 4)
    km_zero['text'] = km_value


#First Text Box for Miles
miles_text = tkinter.Entry(width=5, font=("Arial", 16))
miles_text.focus()
miles_text.grid(column=2, row=2, padx=10, pady=10)

#label
miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=3, row=2)

# label
is_equal_to = tkinter.Label(text="is equal to")
is_equal_to.grid(column=1, row=3)

# miles to km result
km_zero = tkinter.Label(text="0")
km_zero.grid(column=2, row=3)

# KM label
km_label = tkinter.Label(text="Km")
km_label.grid(column=3, row=3)

# Button
button = tkinter.Button(text="Calculate", command=miles_to_km,  font=("Arial", 16, 'normal') )
button.config(bg='white', fg='black')
button.grid(column=2, row=5, padx=10, pady=10)



window.mainloop()