from tkinter import *
import pandas
from random import randint, choice

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
try:
    data = pandas.read_csv("data/To_learn.csv")

except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    data_dict = data.to_dict(orient="records")

else:
    data_dict = data.to_dict(orient="records")


def next_card():
    global  current_card, flip_timer
    current_card = choice(data_dict)
    canva.itemconfig(canva_card, text= "French", fill = "black")
    canva.itemconfig(canva_text, text = current_card["French"], fill = "black")
    canva.itemconfig(Image, image= front)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canva.itemconfig(canva_card, fill = "white", text= "English")
    canva.itemconfig(canva_text, fill = "white",text = current_card["English"])
    canva.itemconfig(Image, image = back)

def is_ok():
    data_dict.remove(current_card)
    next_card()
    new_data = pandas.DataFrame(data_dict)
    new_data.to_csv("data/To_learn.csv", index = False)

window = Tk()
window.title("Flash Cards")
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

canva = Canvas(width=800, height=526)
front = PhotoImage(file = "images/card_front.png")
back = PhotoImage(file = "images/card_back.png")
Image = canva.create_image(400, 263, image = front)
canva_card = canva.create_text(400, 150, text = "",font = ("Ariel" , 40, "italic"))
canva_text = canva.create_text(400, 263, text = "", font = ("Ariel" , 40, "bold"))
canva.config(bg = BACKGROUND_COLOR, highlightthickness= 0)
canva.grid(column = 0, row = 0, columnspan = 2)

wrong = PhotoImage(file = "images/wrong.png")
button_wrong = Button( image = wrong, highlightthickness= 0, border=0, command = next_card)
button_wrong.grid(column = 0, row = 1)

right = PhotoImage(file = "images/right.png")
button_right = Button( image = right, highlightthickness= 0, border=0, command = is_ok)
button_right.grid(column = 1, row = 1)

next_card()


window.mainloop()



