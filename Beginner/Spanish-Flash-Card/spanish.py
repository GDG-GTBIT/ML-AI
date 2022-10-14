BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas as pd
import random

current_card = {}
to_learn = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/spanish_list.csv")
    to_learn =original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


#----------------------Functions----------------------#

def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Spanish", fill="black")
    canvas.itemconfig(card_word, text=current_card["Spanish"], fill="black")
    canvas.itemconfig(card, image=card_front)
    flip_timer = window.after(3000, flip_card)

def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/Words_to_learn.csv",index=False)
    next_card()


def flip_card():
    canvas.itemconfig(card_title,text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white" )
    canvas.itemconfig(card, image=card_back)


#----------------------UI-----------------------------#

window = Tk()
window.title("Flash Card")
window.config( padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

canvas =Canvas(width=800, height=526, highlightthickness=0)

#Screen

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400,263, image=card_front)
canvas.config(bg =BACKGROUND_COLOR)
card_title = canvas.create_text(400, 150, text="Tital", font=("Ariel", 40 , "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 40 , "italic"))
canvas.grid(column=0,row=0, columnspan=2)


#Buttons

right=PhotoImage(file="images/right.png")
known_button = Button(image=right,highlightthickness=0,command=is_known)
known_button.grid(column=1,row=1)

wrong = PhotoImage(file='images/wrong.png')
unknown_button = Button(image=wrong,highlightthickness=0,command=next_card)
unknown_button.grid(column=0,row=1)


next_card()
window.mainloop()