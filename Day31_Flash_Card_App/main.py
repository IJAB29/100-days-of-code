import pandas
from tkinter import *
from random import randint
from tkinter import messagebox

BACKGROUND_COLOR = "#B1DDC6"
FONT_LANGUAGE = ("Arial", 40, "italic")
FONT_WORD = ("Arial", 60, "bold")
randomNum = 0
jpWord = ""
enWord = ""

"""-----------------------------------CSV-----------------------------------"""
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/japanese_words.csv")

"""-----------------------------------FUNCTIONS-----------------------------------"""


def flip():

    canvas.itemconfig(languageLbl, text="English", fill="white")
    canvas.itemconfig(wordLbl, text=enWord, fill="white")
    canvas.itemconfig(imageCanv, image=backImg)


def nextWord():
    global timer, randomNum, jpWord, enWord

    try:
        root.after_cancel(timer)

        randomNum = randint(0, len(data.index)-1)
        jpWord = data["Japanese"].loc[data.index[randomNum]]
        enWord = data["English"].loc[data.index[randomNum]]

        canvas.itemconfig(languageLbl, text="Japanese", fill="black")
        canvas.itemconfig(wordLbl, text=jpWord, fill="black")
        canvas.itemconfig(imageCanv, image=frontImg)

        timer = root.after(3000, flip)

    except ValueError:
        messagebox.showinfo("Notification", "Congratulations, you have learned all the words!")


def right():
    global data
    data = data.drop(data.index[randomNum])
    pandas.DataFrame(data).to_csv("data/words_to_learn.csv", index=False)
    nextWord()


def wrong():
    nextWord()


"""-----------------------------------UI-----------------------------------"""
root = Tk()
root.title("Barry Allen")
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = root.after(3000, flip)

frontImg = PhotoImage(file="images/card_front.png")
backImg = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0)
imageCanv = canvas.create_image(400, 263, image=frontImg)
languageLbl = canvas.create_text(400, 150, font=FONT_LANGUAGE, text="Japanese")
wordLbl = canvas.create_text(400, 263, font=FONT_WORD, text="EHE")
canvas.grid(row=0, column=0, columnspan=2)

"""Buttons"""
wrongImg = PhotoImage(file="images/wrong.png")
wrongBtn = Button(image=wrongImg, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0, command=wrong)
wrongBtn.grid(row=1, column=0)

rightImg = PhotoImage(file="images/right.png")
rightBtn = Button(image=rightImg, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0, command=right)
rightBtn.grid(row=1, column=1)

nextWord()

root.mainloop()
