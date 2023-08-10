from tkinter import *
from tkinter import messagebox
import pandas
import os
import random
import pyperclip
import json


def read():
    with open("data.json", "r") as f:
        return json.load(f)


def write(d):
    with open("data.json", "w") as f:
        json.dump(d, f, indent=4)


"""# ---------------------------- PASSWORD GENERATOR ------------------------------- #"""


def search():
    website = websiteEnt.get()
    try:
        data = read()

    except FileNotFoundError:
        messagebox.showerror("Notification", "No Data File Found.")

    else:
        if len(website) == 0:
            messagebox.showerror("Notification", "Field cannot be empty.")
        elif website not in data:
            messagebox.showerror("Notification", f"No details for {website} found.")
        else:
            messagebox.showinfo(f"{website}", f"Email/Username: {data[website]['Email/Username']}\n"
                                                      f"Password: {data[website]['Password']}")


"""# ---------------------------- PASSWORD GENERATOR ------------------------------- #"""


def passwordGenerator(nr_letters=None, nr_symbols=None, nr_numbers=None):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password = ""
    letList = [random.choice(letters) for i in range(1, nr_letters + 1)]
    numList = [random.choice(numbers) for i in range(1, nr_numbers + 1)]
    symList = [random.choice(symbols) for i in range(1, nr_symbols + 1)]

    password_list = letList + numList + symList
    random.shuffle(password_list)

    password = password.join(password_list)
    pyperclip.copy(password)
    return password


def generate():
    entryText.set(passwordGenerator(5, 5, 5))


"""# ---------------------------- SAVE PASSWORD ------------------------------- #"""


def saveData():
    website = websiteEnt.get()
    email = emailEnt.get()
    password = passwordEnt.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Notification", message="Please don't leave any fields empty.")

    else:

        # dataDF = pandas.DataFrame({"Website": [website], "Email/Username": [email], "Password": [password]})
        #
        # if not os.path.isfile("data.csv") or os.path.getsize("data.csv") == 0:
        #     dataDF.to_csv("data.csv", index=False)
        # else:
        #     dataDF.to_csv("data.csv", mode="a", header=False, index=False)

        newData = {website: {"Email/Username": email, "Password": password}}

        try:
            data = read()

        except (FileNotFoundError, json.decoder.JSONDecodeError):
            write(newData)

        else:
            data.update(newData)
            write(data)

        finally:
            websiteEnt.delete(0, "end")
            passwordEnt.delete(0, "end")

            messagebox.showinfo(title="Notification", message=f"Account from {website} saved.")


"""# ---------------------------- UI SETUP ------------------------------- #"""
root = Tk()
root.title("Password Manager")
root.config(padx=20, pady=20)
root.resizable(0, 0)

entryText = StringVar()

canvas = Canvas(height=200, width=200, highlightthickness=0)
logoImg = PhotoImage(file="logo.png")
logoCan = canvas.create_image(100, 100, image=logoImg)
canvas.grid(row=0, column=1)

websiteLab = Label(text="Website:")
websiteLab.grid(row=1, column=0)

websiteEnt = Entry(width=21)
websiteEnt.grid(row=1, column=1)
websiteEnt.focus()

emailLab = Label(text="Email/Username:")
emailLab.grid(row=2, column=0)

emailEnt = Entry(width=35)
emailEnt.grid(row=2, column=1, columnspan=2)
emailEnt.insert(0, "jayvhik@gmail.com")

passwordLab = Label(text="Password:")
passwordLab.grid(row=3, column=0)

passwordEnt = Entry(width=21, textvariable=entryText)
passwordEnt.grid(row=3, column=1)

generateBtn = Button(text="Generate Password", command=generate, width=14)
generateBtn.grid(row=3, column=2)

addBtn = Button(text="Add", width=30, command=saveData)
addBtn.grid(row=4, column=1, columnspan=2)

searchBtn = Button(text="Search", command=search, width=14)
searchBtn.grid(row=1, column=2)

root.mainloop()
