"""Lab 13.1

This module test the question model.

@author: Keith VanderLinden (kvlinden)
@date: Spring, 2021
"""

from question import ShortAnswer, FillInTheBlank, TrueFalse

q = ShortAnswer('question', 'answer')
assert q.get_question() == 'question?'
assert q.get_answer() == 'answer'
assert not (q.check_answer('blob'))
assert q.check_answer('answer')

q = FillInTheBlank('question', 'answer')
assert q.get_question() == 'question\nFill in the blank.'
assert q.get_answer() == 'answer'
assert not (q.check_answer('blob'))
assert q.check_answer('answer')

q = TrueFalse('question', True)
assert q.get_question() == 'question\nIs this statement true or false?'
assert q.get_answer() == 'True'
assert not (q.check_answer('maybe'))
assert q.check_answer('True')