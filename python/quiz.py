class Quiz:#create a class called Quiz and define the function
    def __init__(self, questions):
        self.question_no = 0 #initialize the question number
        self.score = 0 #intiallly the score is 0
        self.questions = questions
        self.current_question = None #intially set current question is none
    def next_questions(self):
        """To check if the quiz has move to the next questions"""
        
        return self.question_no < len(self.questions)
    def next_question(self):
        """Get the next question by incrementing the question number"""
        
        self.current_question = self.questions[self.question_no]
        self.question_no += 1
        ## unescaping HTML entities
        q_text = self.current_question.question_text #display the question
        return f"Q.{self.question_no}: {q_text}"
    def check_answer(self, user_answer): 
        """Check the user answer and calculate the score"""
        
        correct_answer = self.current_question.correct_answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
           
        else:
            return False
    def get_score(self):
        """Get the number of correct answers, wrong answers and score percentage."""
        wrong = self.question_no - self.score
        score_percent = int(self.score / self.question_no * 100)
        return (self.score, wrong, score_percent)