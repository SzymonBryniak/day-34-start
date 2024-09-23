import tkinter
from tkinter import *


THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.geometry("350x500")

        self.photo1 = PhotoImage(file="./images/true.png")
        self.photo2 = PhotoImage(file="./images/false.png")

        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.canvas = Canvas(self.window, width=300, height=250)
        self.canvas.grid(column=0, row=1, columnspan=2)

        self.score = tkinter.Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0, sticky=E)

        self.green_button = tkinter.Button(image=self.photo1)
        self.green_button.grid(column=0, row=2)

        self.red_button = tkinter.Button(image=self.photo2)
        self.red_button.grid(column=1, row=2)
        self.window.mainloop()
