"""Lab 13.1

This module test the quiz model.

@author: Keith VanderLinden (kvlinden)
@date: Spring, 2021
"""

from quiz import Quiz

quiz = Quiz()

# The questions should have correct answers.
while quiz.has_next():
    assert quiz.check_current_answer(quiz.get_current_answer())
    quiz.next()
