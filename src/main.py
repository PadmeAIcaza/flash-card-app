from tkinter import *

BG = "#BFE6D6"
T_FONT = ('Times New Roman', 40, 'italic')
W_FONT = ('Times New Roman', 60, 'bold')

window = Tk()
window.title("Flashcard")
window.config(padx=50, pady=50, bg=BG)

# CARD
canvas = Canvas(window, width=800, height=526, bg=BG, highlightthickness=0)
card_img = PhotoImage(file="../images/card_front.png")
canvas.create_image(400, 263, image=card_img)  # center-ish
canvas.grid(row=0, column=0, columnspan=3)

# Text
canvas.create_text(400, 150, text="French", font=T_FONT)
canvas.create_text(400, 263, text="trouve", font=W_FONT)

# Buttons
correct = PhotoImage(file="../images/right.png")
correct_button = Button(window, image=correct, bd=0, highlightthickness=0, bg=BG, activebackground=BG)
correct_button.grid(row=1, column=2)

wrong = PhotoImage(file="../images/wrong.png")
wrong_button = Button(window, image=wrong, bd=0, highlightthickness=0, bg=BG, activebackground=BG)
wrong_button.grid(row=1, column=0)

window.mainloop()
