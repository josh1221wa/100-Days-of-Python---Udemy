from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain:QuizBrain):   # We use the : to set the datatype of the argument
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(self.window,text="Score : 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(self.window, bg="white", height=250, width=300)
        self.question_text = self.canvas.create_text(150, 125, text="Some Question Text", font=("Arial", 15, "italic"), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_icon = PhotoImage(file=r"Day 34\Day_34_Project\images\true.png")
        self.true_but = Button(image=true_icon, bg=THEME_COLOR, highlightthickness=0, command=self.true_clicked)
        self.true_but.grid(row=2, column=0)

        false_icon = PhotoImage(file=r"Day 34\Day_34_Project\images\false.png")
        self.false_but = Button(image=false_icon, bg=THEME_COLOR, highlightthickness=0, command=self.false_clicked)
        self.false_but.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_but.config(state="disabled")
            self.false_but.config(state="disabled")

    def true_clicked(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    
    def false_clicked(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right == True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
