import html
from textwrap import wrap


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score_brain = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def first_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        # user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        user_question = f"Q.{self.question_number}: {q_text} (True/False): "
        # self.check_answer()  # I need to pass the answer to this function
        return '\n'.join(wrap(user_question, width=25))

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        # user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        user_question = f"Q.{self.question_number}: {q_text} (True/False): "
        # self.check_answer()  # I need to pass the answer to this function
        return '\n'.join(wrap(user_question, width=25))

    def check_answer(self, user_answer):
        score = 0
        correct_answer = self.current_question.answer
        if user_answer == correct_answer:
            self.score_brain += 1
            return f"You got it right! Your current score is: {self.score_brain}/{self.question_number}"
        else:
            return f"That's wrong. Your current score is: {self.score_brain}/{self.question_number}"

        # print(f"Your current score is: {self.score}/{self.question_number}")
        # print("\n")
