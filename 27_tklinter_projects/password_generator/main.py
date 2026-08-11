import tkinter
from tkinter import messagebox
from random import shuffle, random, randint,choice
import string

import json

letters = list(string.ascii_lowercase)
numbers = list(string.digits)
symbols = ['!','@','#','$','%','^','&','*','(',')','-','+']


window = tkinter.Tk()
window.title("Password Generator")



def generate_passwrod():

    mixed_arr = []
    pass_letter = [choice(letters) for _ in range(randint(8,10))]
    pass_numbers = [choice(numbers) for _ in range(randint(2,4))]
    pass_symbols = [choice(symbols) for _ in range(randint(2,4))]
    password_list = pass_letter + pass_numbers + pass_symbols
    shuffle(password_list)

    password = "".join(password_list)
    print(password)
    password_txt.delete(0, tkinter.END)
    password_txt.insert(0, password)


def save_to_file():
    website  = website_txt.get()
    email = email_txt.get()
    password = password_txt.get()
    json_data = {website:{
        "email":email,
        "password":password
    }}
    if (len(password) ==0) or (len(email) ==0) or (len(website)==0):
        messagebox.showerror(title="Error", message="Please fill all the details: email, password, and website")

    
    else:            
        # is_ok = messagebox.askokcancel(title="Success", message=f"These are the details: Email:{email}, Passwrod:{password} and Website:{website}. Do you want to save it?")
        # if is_ok:
        #     with open('./data.txt', 'a') as f:
        #         f.write(f"{website} | {email} | {password}\n")
        #     website_txt.delete(0,tkinter.END)
        #     email_txt.delete(0,tkinter.END)
        #     password_txt.delete(0, tkinter.END)
        #     messagebox.showinfo(title="Success", message="Data saved successfully!")
        with open('./data.json', 'r') as data_file:

            # Reading data from json file...
            data = json.load(data_file)
            # Updating...
            data.update(json_data)
        
        with open('./data.json', 'w') as data_file:
            # Saving updating data..
            json.dump(data, data_file, indent=4)

            messagebox.showinfo(title="Success", message="Data saved successfully!")
            website_txt.delete(0,tkinter.END)
            email_txt.delete(0,tkinter.END)
            password_txt.delete(0, tkinter.END)


# window.minsize(width=400, height=400)
window.config(padx=50, pady=50)
canvas = tkinter.Canvas(width=200, height=200)
lock_img = tkinter.PhotoImage(file='./logo.png')
canvas.create_image(100,100,image=lock_img)
canvas.grid(row=0, column=1)



website_label = tkinter.Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = tkinter.Label(text="Email/Username:")
email_label.grid(column=0, row=2, )
password_label = tkinter.Label(text="Password:")
password_label.grid(column=0, row=3)


website_txt = tkinter.Entry(width=35)
website_txt.grid(row=1,column=1, columnspan=2, ipady=4)
website_txt.focus()
email_txt = tkinter.Entry(width=35)
email_txt.grid(row=2,column=1, columnspan=2, ipady=4)
password_txt = tkinter.Entry(width=35)
password_txt.grid(row=3,column=1, columnspan=2, ipady=4)


generate_password_btn = tkinter.Button(text="Generate Password", command=generate_passwrod)
generate_password_btn.grid(row=3, column=3)

# Add btn
add_btn = tkinter.Button(text="Add", width=32, command=save_to_file)
add_btn.grid(row=4, column=1, columnspan=2, pady=5)



window.mainloop()