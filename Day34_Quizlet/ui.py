import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 13, "bold")
FONT_QUESTION = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.root = tk.Tk()
        self.root.title("Quiz")
        self.root.resizable(False, False)
        self.root.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = tk.Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white", font=FONT)
        self.score_label.grid(column=1, row=0)

        self.canvas = tk.Canvas(height=250, width=300, borderwidth=0, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, font=FONT_QUESTION)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=25)

        self.true_image = tk.PhotoImage(file="images/true.png")
        self.false_image = tk.PhotoImage(file="images/false.png")

        self.true_button = tk.Button(image=self.true_image, borderwidth=0, bg=THEME_COLOR, command=self.answer_true)
        self.true_button.grid(column=0, row=2)
        self.false_button = tk.Button(image=self.false_image, borderwidth=0, bg=THEME_COLOR, command=self.answer_false)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.root.mainloop()

    def get_next_question(self):
        self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())

    def answer_true(self):
        self.check(self.quiz.check_answer("True"))

    def answer_false(self):
        self.check(self.quiz.check_answer("False"))

    def update_screen(self):
        try:
            self.get_next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
        except IndexError:
            self.canvas.itemconfig(self.question_text, text="You've reached the end.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        finally:
            self.canvas.config(bg="white")

    def check(self, correct):
        if correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.root.after(1000, self.update_screen)
