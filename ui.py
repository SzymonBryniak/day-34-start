import tkinter
from tkinter import *
from PIL import Image, ImageTk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface(QuizBrain):

    def __init__(self, q_list):
        super().__init__(q_list)
        self.window = Tk()

        self.window.title("Quizzler")
        self.window.geometry("350x500")
        # PIL start
        self.red = (Image.open("./images/false.png"))
        self.green = (Image.open("./images/true.png"))
        self.resized_red = self.red.resize((80, 80))
        self.resized_green = self.green.resize((80, 80))
        self.new_green = ImageTk.PhotoImage(self.resized_green)
        self.new_red = ImageTk.PhotoImage(self.resized_red)
        # PIL end
        self.window.config(bg=THEME_COLOR, padx=20, pady=40)

        self.canvas = Canvas(self.window, width=300, height=250)
        self.canvas.create_text(150, 50, text=self.next_question(), font='Helvetica 15 bold', fill="black")
        # self.canvas.create_text(120, 50, text=self.next_question(), font='Helvetica 15 bold', fill="black")

        self.canvas.grid(column=0, row=1, columnspan=2)
        # widgets
        self.score = tkinter.Label(text="Score: 0", bg=THEME_COLOR, fg="white", anchor=CENTER)
        self.score.grid(column=1, row=0, sticky=SE)

        self.green_button = tkinter.Button(image=self.new_green, border=0, borderwidth=0, background="green")
        self.green_button.place(x=40, y=305)

        self.red_button = tkinter.Button(image=self.new_red, border=0, background="red", anchor=S)
        self.red_button.place(x=200, y=305)

        self.window.mainloop()

    def display_question(self):
        if self.still_has_questions():
            self.canvas.create_text(70, 70, text=self.next_question(), font='Helvetica 15 bold', fill="black")
        return

    def display_score(self, score):
        self.score.configure(text=f"Score: {score}")
        return
