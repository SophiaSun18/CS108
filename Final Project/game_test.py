"""CS 108 Final Project Game Test

This module implements some test cases for the room-escape game functions.

@author: ZeAi Sun (zs35)
@date: Fall, 2021
"""

from room_model import Room
from game_model import Game
import random

room = Room()
game = Game()

# Test the constructor of the Room class.
assert room.walls_info[0][0] == 'upper wall'
assert '\n' not in room.walls_info
assert len(room.walls_info) == 4
assert room.furs_info[-1][-(len(room.furs_info[-1]))] == 'entrance'

for i in room.furs_info:
    assert len(i) == 6

# Test the constructor of the Game class.
assert len(game.count) == len(room.furs_info)
assert game.count['door'] == 0

# Test the usability of the get_fur_name method.
# When get_fur_name function returns 'bed', the value of 'bed' in self.count should increase by 1.
assert game.get_fur_name(100,100) == ('bed')
assert game.get_fur_name(250,50) == None
assert game.count['bed'] == 1

# Test the usability of the get_info method.
# Call the get_fur_name method multiple times to test if the given information changes based on how many times the method is called.
assert game.get_fur_name(580,200) == ('window')
assert game.get_info('window') == 'The sky is dark. It is snowing outside.'
assert game.get_fur_name(580,200) == ('window')
assert game.get_info('window') == 'You can not get out of the window, but your hand can.'
assert game.get_fur_name(580,200) == ('window')
assert game.get_info('window') == 'Snow has piled up on the outside windowsill.'
assert game.get_fur_name(580,200) == ('window')
assert game.get_info('window') == 'You try to put your hand out, and your hand immediately get wet and cold.'

# Test the usability of the get_item method.
assert game.get_item('wardrobe') == ('A scissor.')
assert game.get_item('bed') == None

# Test the usability of get_interaction method.
assert game.get_interaction('A piece of rusted wire.',
                            'A locked box.') == ('You opened the box and get a piece of empty paper.',
                                                 ['A locked box.', 'A piece of rusted wire.'],
                                                 ['A piece of empty paper.'])
assert game.get_interaction('A piece of dirty glass.',
                            'A piece of paper with little words.') == ('You can not use this item here now.',
                                                                       [], [])

# Test the usability of the save_game and load_game methods.
list = game.load_game()
print(list)
assert game.load_game() == ([], [])
game.save_game(['Info 1', 'Info 2', 'Info 3'], ['Item 1', 'Item 2', 'Item 3.'])
f = open('save.txt')
lines = f.readlines()
assert len(lines) == 2
# assert game.load_game == ['Info 1', 'Info 2', 'Info 3'], ['Item 1', 'Item 2', 'Item 3']