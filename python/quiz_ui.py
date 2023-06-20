#here using interface tkinter framework and widgets
from tkinter import Tk, Canvas, StringVar, Label, Radiobutton, Button, messagebox
from quiz import Quiz
THEME_COLOR = "#0000ff"
class QuizUi:
    def __init__(self, quiz_brain: Quiz) -> None:
        self.quiz = quiz_brain
        self.master = Tk()
        self.master.title("Computer Quiz App")
        self.master.geometry("950x630")#size of the GUI window
        # Display Title rules
        self.display_title()
        self.display_rules()
        self.display_question()
        # Declare a StringVar to store user's answer
        self.user_answer = StringVar()
        # Display four options(radio buttons)
        self.opts = self.radio_buttons()
        self.display_options()
        # To show whether the answer is correct or wrong
        self.feedback = Label(self.master, pady=10, font=("ariel", 12, "bold"))
        self.feedback.place(x=580, y=380)
        self.buttons()
        # Mainloop
        self.master.mainloop()
    def display_title(self):
        """To display title"""
        # Title
        title = Label(self.master, text="Computer Science Quiz Application",
                      width=60, bg="blue", fg="white", font=("ariel", 20, "bold"))
        # place of the title
        title.place(x=0, y=2)
        # place of the rules
    def display_rules(self):
        rules = Label(self.master, text="Instruction:\n1. You will be asked a series of questions.\n"
                      "2. You have to select one option out of four.\n"
                      "3. You will get one points for each correct answer.\n"
                      "4. There is no negative marking for wrong answers.\n"
                      "5. You can quit the quiz anytime by clicking on the Quit button.Gook Luck!", 
                      width=100, bg="green", fg="white", 
                      font=("ariel", 12, "bold"))
        rules.grid(pady=(50,70))
        self.canvas = Canvas(width=800, height=150)
        self.question_text = self.canvas.create_text(250, 70,
                                                     text="",
                                                       width=480,
                                                     fill=THEME_COLOR,
                                                     font=(
                                                         'Ariel', 15, 'italic')
                                                     )
        self.canvas.grid(row=2, column=0, columnspan=2, pady=2)
     
    def display_question(self):
        """To display the question"""
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
    def radio_buttons(self):
        """To create four options (radio buttons)"""
        # initialize the list with an empty list of options
        choice_list = []
        # position of the first option
        y_pos = 350
        # adding the options to the list
        while len(choice_list) < 4:
            # setting the radio button properties
            radio_btn = Radiobutton(self.master, text="", variable=self.user_answer,
                                    value='', font=("ariel", 14))
            # adding the button to the list
            choice_list.append(radio_btn)
            # placing the button
            radio_btn.place(x=200, y=y_pos)
            # incrementing the y-axis position by 40
            y_pos += 40
        # return the radio buttons
        return choice_list
    def display_options(self): #To display four options
        val = 0
        self.user_answer.set(None)# deselecting the options
        # looping over the options to be displayed for the
        # text of the radio buttons.
        for option in self.quiz.current_question.choices:
            self.opts[val]['text'] = option
            self.opts[val]['value'] = option
            val += 1
    def next_btn(self):
        """To show feedback for each answer and keep checking for more questions"""
        # Check if the answer is correct
        if self.quiz.check_answer(self.user_answer.get()):
            self.feedback["fg"] = "green"
            self.feedback["text"] = 'Correct answer! \U0001F44D'
        else:
            self.feedback['fg'] = 'red'
            self.feedback['text'] = ('Oops! \n'
                                     f'The correct answer is: {self.quiz.current_question.correct_answer}')
        if self.quiz.next_questions():
            # Moves to next to display next question and its options
            self.display_question()
            self.display_options()
        else:
            # if no more questions, then it displays the score
            self.display_result()
            # destroys the self.window
            self.master.destroy()
    def buttons(self):
        """To show next button and quit button"""
        next_button = Button(self.master, text="Next", command=self.next_btn,
                             width=10, bg="green", fg="white", font=("ariel", 16, "bold"))
        # palcing the button  on the screen
        next_button.place(x=550, y=560)
        # This is the second button which is used to Quit the self.window
        quit_button = Button(self.master, text="Quit", command=self.master.destroy,
                             width=5, bg="red", fg="white", font=("ariel", 16, " bold"))
        # placing the Quit button on the screen
        quit_button.place(x=600, y=220)
      
    def display_result(self):
        """To display the result using messagebox"""
        correct, wrong, score_percent = self.quiz.get_score()
        correct = f"Correct: {correct}"
        wrong = f"Wrong: {wrong}"
        # calculates the percentage of correct answers
        result = f"Score: {score_percent}%"
        # Shows a message box to display the result
        messagebox.showinfo("Result", f"{result}\n{correct}\n{wrong}")
    