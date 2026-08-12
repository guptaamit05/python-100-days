from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
data_dict ={}
current_crd = {}

try:
    data = pandas.read_csv('./data/words_to_learn.csv')

except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    data_dict = original_data.to_dict(orient='records')

else:
    data_dict = data.to_dict(orient='records')


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)



def next_card():
   global current_crd, flip_cancel
   window.after_cancel(flip_cancel)
   current_crd =  random.choice(data_dict)
   canvas.itemconfig(card_text, text="French", fill="black")
   canvas.itemconfig(meaning, text=current_crd['French'], fill="black")
   canvas.itemconfig(canvas_img, image=bg_front_image)
   flip_cancel= window.after(3000, flip_card)

def flip_card():
   canvas.itemconfig(card_text, text="English", fill="white")
   canvas.itemconfig(meaning, text=current_crd['English'], fill="white")
   canvas.itemconfig(canvas_img, image=bg_back_image)

def is_known():
    data_dict.remove(current_crd)
    new_data = pandas.DataFrame(data_dict)
    print(len(new_data))
    new_data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


flip_cancel = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526)
bg_front_image = PhotoImage(file='./images/card_front.png')
bg_back_image = PhotoImage(file="./images/card_back.png")
canvas_img = canvas.create_image(400,263, image=bg_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_text = canvas.create_text(400, 150,  font=('Arial', 20, 'italic'))
meaning =   canvas.create_text(400, 263,  font=('Arial', 30, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

# left button (Cancel button)
cancel_btn_img = PhotoImage(file="./images/wrong.png")
cancel_button = Button(image=cancel_btn_img, text="I Know", highlightthickness=0, command=next_card)
cancel_button.grid(row=1, column=0)


known = canvas.create_text(200, 510,  text="UnKnown", font=('Arial', 10, 'bold'))
unknown = canvas.create_text(600, 510, text="Know", font=('Arial', 10, 'bold'))


# right button
right_btn_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_btn_img, text="Unknown", highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)



next_card()



window.mainloop()