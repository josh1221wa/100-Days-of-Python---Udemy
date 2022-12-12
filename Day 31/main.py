from tkinter import *
import pandas as pd
from random import choice
from time import sleep

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pd.read_csv(r"Day 31/data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv(r"Day 31/data/french_words.csv")
to_learn = data.to_dict(orient="records")

def next_card():
    global card, window, word_choice, flip_timer
    window.after_cancel(flip_timer)
    word_choice = choice(to_learn)
    new_word = word_choice["French"]
    card.itemconfig(lang, text="French", fill="black")
    card.itemconfig(word, text=new_word, fill="black")
    card.itemconfig(card_bg, image=front_img)
    flip_timer = window.after(3000, flip_card)    

def known_word():
    to_learn.remove(word_choice)
    next_card()

def flip_card():
    new_word = word_choice["English"]
    card.itemconfig(lang, text="English", fill="white")
    card.itemconfig(word, text=new_word, fill="white")
    card.itemconfig(card_bg, image=back_img)

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

front_img = PhotoImage(file=r"Day 31/images/card_front.png")
back_img = PhotoImage(file=r"Day 31/images/card_back.png")

card = Canvas(window, width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_bg = card.create_image(400, 263, image=None)
card.grid(row=0, column=0, columnspan=2, sticky=EW)

lang = card.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = card.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

wrong_img = PhotoImage(file=r"Day 31/images/wrong.png")
wrong_but = Button(image=wrong_img, highlightthickness=0, bd=0, command=next_card)
wrong_but.grid(row=1, column=0)

right_img = PhotoImage(file=r"Day 31/images/right.png")
right_but = Button(image=right_img, highlightthickness=0, bd=0, command=known_word)
right_but.grid(row=1, column=1)

next_card()

window.mainloop()

new_data = pd.DataFrame.from_dict(data=to_learn, orient="columns")  # type: ignore
new_data.to_csv(r"Day 31/data/words_to_learn.csv", index=False)