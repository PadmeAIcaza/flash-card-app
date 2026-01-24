from tkinter import *
import pandas as pd
import random

BG = "#91C2AF"
T_FONT = ('Times New Roman', 40, 'italic')
W_FONT = ('Times New Roman', 60, 'bold')

# Data
data = pd.read_csv('../data/french_words.csv')
words_list = data.to_dict(orient='records')

current_card = {}
flip_timer = None

def next_card():
    global current_card, flip_timer

    current_card = random.choice(words_list)

    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_img, image=card_front)

    if flip_timer is not None:
        window.after_cancel(flip_timer)

    flip_timer = window.after(3000, flip_card)

def flip_card():
    global current_card

    canvas.itemconfig(canvas_img, image=card_back)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")


window = Tk()
window.title("Flashcard")
window.config(padx=50, pady=50, bg=BG)

# CARD
canvas = Canvas(window, width=800, height=526, bg=BG, highlightthickness=0)
card_back = PhotoImage(file="../images/card_back.png")
card_front = PhotoImage(file="../images/card_front.png")
canvas_img = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=3)

# Text
title = canvas.create_text(400, 150, text="French", font=T_FONT)
word = canvas.create_text(400, 263, text="trouve", font=W_FONT)

# Buttons
correct = PhotoImage(file="../images/right.png").subsample(15, 15)
correct_button = Button(window, image=correct, bd=0, highlightthickness=0,
                        bg=BG, activebackground=BG, command=next_card)
correct_button.grid(row=1, column=2)

wrong = PhotoImage(file="../images/wrong.png").subsample(15, 15)
wrong_button = Button(window, image=wrong, bd=0, highlightthickness=0,
                      bg=BG, activebackground=BG, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()
window.mainloop()
