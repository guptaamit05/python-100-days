from tkinter import *
import requests
from tkinter import messagebox

window = Tk()

window.config(padx=50, pady=50)
window.title("Kanye App..")

def get_quote():
    try:
        response = requests.get("https://api.kanye.rest/")
        # response.raise_for_status()
        if not response.status_code ==200:
            canvas.itemconfig(quote_txt, text="Something went wrong! try after some time")
        else:
            quote = response.json()['quote']
            canvas.itemconfig(quote_txt, text=quote,)
    except Exception as e:
        messagebox.showerror(title="Error", message=f"Error: {e}")
        print("Error:", e)

canvas = Canvas(width=300, height=414)
bg_img = PhotoImage(file="./background.png")
canvas.create_image(150, 207, image=bg_img)
quote_txt = canvas.create_text(150, 207, text="Kanye Quote goes here", width=250, font=('Arial', 14, 'bold'), fill='white')
canvas.grid(row=0, column=0)

btn_img = PhotoImage(file="./kanye.png")
# button = Button(image=btn_img, highlightthickness=0, border=0)
button = Button(image=btn_img, highlightthickness=0,  command=get_quote)
button.grid(row=1, column=0)


get_quote()

window.mainloop()