"""CS 108 - Lab 8

This module runs a command-line interface that controls successive image
processing commands. The image is redisplayed after each command.

@author: Keith VanderLinden (kvlinden) and Ken Arnold (ka37)
@date: Spring, 2020
"""

from image_processing import *


MENU = 'b - Brighten' \
       '\nd - Darken' \
       '\nfh - Flip Horizontal' \
       '\nq - Quit'

image = load_image('images/sydney_sunset.png')

# Run a CLI loop, allowing the user to repeat commands by hitting enter.
previous_command = ''
while True:
    print('Close the image window to proceed.')
    display_image(image)
    print(MENU)
    command = input('Command: ').lower()

    if command == '':
        command = previous_command

    if command == 'b':
        image = brighten(image)
    elif command == 'd':
        image = dim(image)
    elif command == 'fh':
        image = flip_horizontal(image)
    elif command == 'q':
        break
    else:
        print('invalid command')

    previous_command = command
