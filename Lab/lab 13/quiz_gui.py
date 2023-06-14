""" Lab 13.1

This module implements a quiz application with different sorts of questions.

@author: Keith VanderLinden (kvlinden)
@date: Summer, 2015
@date: Spring, 2021 - ported to GuiZero
"""

from guizero import App, Text, TextBox, PushButton, Box
from quiz import Quiz


class QuizApp:
    """This class builds the quiz application GUI."""

    def __init__(self, app):
        """Instantiates the GUI widgets"""

        app.title = 'World Forum Quiz'
        app.width = 400
        app.height = 200
        app.font = 'Helvetica'
        app.text_size = 12

        # Build the quiz to be given.
        self.quiz = Quiz()

        # Keep track of the user's performance.
        self.correct_count = 0
        self.question_count = 0

        # Build the GUI.
        self.question_text = TextBox(app, multiline=True,
                                     width=app.width, height=6)
        self.question_text.value = self.quiz.get_current_question()
        box = Box(app, layout='grid')
        self.answer = TextBox(box, width=30, grid=[0, 0])
        self.enter_button = PushButton(box, self.check_answer,
                                       text='Enter', grid=[1, 0])
        self.instructions = TextBox(app, width=app.width)
        self.instructions.value = 'Welcome to the World Forum quiz!'

    def check_answer(self):
        """Checks the user's answer, gives appropriate feedback, and then
        decides whether to go on with the quiz or print the final score.
        """

        # Check the given answer.
        if self.quiz.check_current_answer(self.answer.value):
            self.instructions.value = 'Good job!  Next question...'
            self.correct_count += 1
        else:
            self.instructions.value = 'Sorry, the answer was ' \
                                      + self.quiz.get_current_answer() \
                                      + '.'
        self.question_count += 1
        self.answer.value = ''

        # Go to the next question if it exists, otherwise print the score.
        self.question_text.clear()
        if self.quiz.has_next():
            self.quiz.next()
            self.question_text.value = self.quiz.get_current_question()
        else:
            self.question_text.value = \
                'Quiz Complete\n' + 'You got {0} correct out of {1}'.format(
                    self.correct_count, self.question_count) + '.'
            self.enter_button.enabled = False
            self.answer.value = ''
            self.instructions.value = ''


app = App()
QuizApp(app)
app.display()
