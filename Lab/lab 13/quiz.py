"""Lab 13.1

This module implements and instantiates a quiz of heterogeneous questions.

@author: Keith VanderLinden (kvlinden)
@date: Summer, 2015
@date: Spring, 2020 - restored original questions
@date: Spring, 2021 - ported to GuiZero; factored out tests
"""

import random
from question import ShortAnswer, FillInTheBlank, TrueFalse


class Quiz:
    """This class builds a quiz model with hard-coded, sample questions.
    TODO: Build a quiz administration GUI that manages the question bank.
    """

    def __init__(self):
        """Initializes the quiz object with sample questions in random order"""

        self.questions = [
            ShortAnswer(
                'Who won the English football cup in 1949',
                'Wolverhampton'),
            FillInTheBlank(
                'The country with the largest population is __________.',
                'China'),
            TrueFalse(
                'The highest mountain in the world is Mount Everest',
                'True')
        ]
        random.shuffle(self.questions)

        self.problemNum = 0

    def get_current_question(self):
        """Returns the text of the current question"""
        return self.questions[self.problemNum].get_question()

    def get_current_answer(self):
        """Returns the answer of the current question"""
        return self.questions[self.problemNum].get_answer()

    def check_current_answer(self, answer):
        """Returns a boolean indicating the correctness of the given answer"""
        return self.questions[self.problemNum].check_answer(answer)

    def has_next(self):
        """Returns a boolean indicating whether there are more questions"""
        return self.problemNum < len(self.questions) - 1

    def next(self):
        """Goes on to the next question"""
        if self.problemNum == len(self.questions) - 1:
            raise StopIteration("There are no more problems")
        self.problemNum += 1
