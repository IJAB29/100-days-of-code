from tkinter import *
import math

"""# ---------------------------- CONSTANTS ------------------------------- #"""
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK = 25 * 60
SHORT_BREAK = 5 * 60
LONG_BREAK = 20 * 60
REPS = 0
COUNTING_DOWN = False
TIMER_STATE = None

"""# ---------------------------- TIMER RESET ------------------------------- #"""


def resetTimer():
    global COUNTING_DOWN
    global REPS
    global TIMER_STATE
    COUNTING_DOWN = False
    REPS = 0
    root.after_cancel(TIMER_STATE)
    completedTasksLab.config(text="")
    taskLab.config(text="Task", fg=GREEN)
    canvas.itemconfig(timerCan, text="00:00")


"""# ---------------------------- TIMER MECHANISM ------------------------------- #"""


def startTimer():
    global REPS
    global COUNTING_DOWN

    if not COUNTING_DOWN:
        REPS += 1
        if REPS % 8 == 0:
            taskLab.config(text="Rest", fg=RED)
            countDown(LONG_BREAK)
        elif REPS % 2 == 0:
            completedTasksLab.config(text=completedTasksLab.cget("text") + "✔")
            taskLab.config(text="Break", fg=PINK)
            countDown(SHORT_BREAK)
        else:
            taskLab.config(text="Work", fg=GREEN)
            countDown(WORK)


"""# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #"""


def countDown(count):
    global COUNTING_DOWN
    global TIMER_STATE

    COUNTING_DOWN = True
    minutes = math.floor(count / 60)
    seconds = count % 60

    if count > 0:
        TIMER_STATE = root.after(1000, countDown, count - 1)
    else:
        COUNTING_DOWN = False
        startTimer()

    if minutes < 10:
        minutes = f"0{minutes}"
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timerCan, text=f"{minutes}:{seconds}")


"""# ---------------------------- UI SETUP ------------------------------- #"""
root = Tk()
root.title("Kamatis")
root.config(padx=100, pady=50, bg=YELLOW)
root.resizable(0, 0)

taskLab = Label(text="Task", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "normal"))
taskLab.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
tomatoCan = canvas.create_image(100, 112, image=image)
timerCan = canvas.create_text(100, 130, fill="white", font=(FONT_NAME, 35, "bold"), text="00:00")
canvas.grid(row=1, column=1)

startBtn = Button(text="Start", fg=PINK, command=startTimer, font=(FONT_NAME, 10, "bold"), highlightthickness=0)
startBtn.grid(row=2, column=0)

resetBtn = Button(text="Reset", fg=PINK, command=resetTimer, font=(FONT_NAME, 10, "bold"), highlightthickness=0)
resetBtn.grid(row=2, column=2)

completedTasksLab = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "normal"))
completedTasksLab.grid(row=3, column=1)

root.mainloop()
