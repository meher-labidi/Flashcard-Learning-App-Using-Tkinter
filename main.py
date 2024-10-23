from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
timer = None
R_W = {}
to_learn = {}


try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def generate_random_word():
    global R_W, flip_timer
    window.after_cancel(flip_timer)
    R_W = random.choice(to_learn)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=R_W["French"], fill="black")
    canvas.itemconfig(image, image=image_1)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=R_W["English"], fill="white")
    canvas.itemconfig(image, image=image_2)


def is_known():
    to_learn.remove(R_W)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    generate_random_word()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
image_1 = PhotoImage(file="images/card_front.png")
image_2 = PhotoImage(file="images/card_back.png")
image = canvas.create_image(400, 275, image=image_1)
title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
my_image_x = PhotoImage(file="./images/wrong.png")
button_x = Button(image=my_image_x, highlightthickness=0, command=generate_random_word)
button_x.grid(row=1, column=0)
my_image_y = PhotoImage(file="images/right.png")
button_y = Button(image=my_image_y, highlightthickness=0, command=is_known)
button_y.grid(row=1, column=1)

generate_random_word()
window.mainloop()
