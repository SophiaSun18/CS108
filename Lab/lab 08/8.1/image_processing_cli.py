"""CS 108 - Lab 8

This module runs a command-line interface that controls successive image
processing commands. The image is redisplayed after each command.

@author: Keith VanderLinden (kvlinden) and Ken Arnold (ka37)
@author: ZeAi Sun (zs35)
@date: Fall, 2021
"""

from image_processing import *


MENU = 'cb - Change Brightness' \
       '\nfh - Flip Horizontal' \
       '\nfv - Flip Vertical' \
       '\nn - Negative' \
       '\ngs - Gray Scale' \
       '\nsn - Snow' \
       '\nse - Sepia' \
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

    if command == 'cb':
        num = int(input('Please enter an integer indicating the desired magnitude of change (positive = brighten, negative = dim): '))
        image = change_brightness(image, num)
    elif command == 'fh':
        image = flip_horizontal(image)
    elif command == 'fv':
        image = flip_vertical(image)
    elif command == 'n':
        image = negative(image)
    elif command == 'gs':
        image = gray_scale(image)
    elif command == 'sn':
        image = snow(image)
    elif command == 'se':
        image = sepia(image)
    elif command == 'q':
        break
    else:
        print('invalid command')

    previous_command = command
