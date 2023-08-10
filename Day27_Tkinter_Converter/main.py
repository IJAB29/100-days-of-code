import tkinter
from tkinter import *

root = Tk()
root.title("Mile to Km Converter")
root.resizable(0, 0)
root.config(padx=15, pady=15)


def convert():
    output.config(text=int(input.get()) * 1.61)


input = Entry(width=10, justify=tkinter.CENTER)
input.grid(column=1, row=0, padx=5, pady=5)

mileText = Label(text="Miles")
mileText.grid(column=2, row=0, padx=5, pady=5)

label = Label(text="is equal to")
label.grid(column=0, row=1, padx=5, pady=5)

output = Label(text="0")
output.grid(column=1, row=1, padx=5, pady=5)

kmLabel = Label(text="Km")
kmLabel.grid(column=2, row=1, padx=5, pady=5)

calcButton = Button(text="Calculate", command=convert)
calcButton.grid(column=1, row=2, padx=5, pady=5)

root.mainloop()
