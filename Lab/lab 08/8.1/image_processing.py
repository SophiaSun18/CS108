"""CS 108 - Lab 8

This module implements image processing functions using the Python Imaging
Library (PIL) to load and display images, and NumPy to manipulate the image's
2D array of pixels. Each pixel is represented as a list of intensity values
for red, green and blue (RGB), each value between 0 (low intensity) and 255 (
high intensity). For example:
    [0, 0, 0] represents black
    [255, 255, 255] represents white
    [255, 0, 0] represents red

@author: Keith VanderLinden (kvlinden) and Ken Arnold (ka37)
@author: ZeAi Sun (zs35)
@date: Fall, 2021 - ported from Java/Processing, Fall, 2010
"""


from PIL import Image
import numpy as np
from copy import deepcopy
from guizero import App, Picture


def load_image(filename):
    """ This function loads an image from the specified file. """

    # Convert pixel values to integer format in order to
    # allow arithmetic that may overflow np's default uint8.
    return np.array(Image.open(filename), dtype='int32')


def display_image(image_array):
    """ This function displays the given image in a separate GuiZero window. """

    # Clip pixel values back to 8-bit range for display.
    image = Image.fromarray(np.uint8(np.clip(image_array, 0, 255)))

    # Show the image in a guizero window.
    app = App(width=image_array.shape[1], height=image_array.shape[0])
    Picture(app, image=image)
    # Bring the guizero window to the front
    # https://stackoverflow.com/a/36191443/69707
    root = app.tk
    root.lift()
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)
    app.display()

def change_brightness(image, num):
    '''This function changes the brightness of the given image.'''
    
    num_rows = len(image)
    num_columns = len(image[0])
    
    # Change each RGB pixel value based on the user input.
    for row_index in range(num_rows):
        for column_index in range(num_columns):
            rgb = image[row_index][column_index]
            image[row_index][column_index] = [rgb[0] + num, rgb[1] + num, rgb[2] + num]

    return image

def negative(image):
    '''This function produces a negative image of the original.'''
    
    num_rows = len(image)
    num_columns = len(image[0])
    
    # Invert each RGB pixel value.
    for row_index in range(num_rows):
        for column_index in range(num_columns):
            rgb = image[row_index][column_index]
            image[row_index][column_index] = [255 - rgb[0], 255 - rgb[1], 255 - rgb[2]]

    return image

def gray_scale(image):
    '''This function removes the RGB color difference in the image.'''
    
    num_rows = len(image)
    num_columns = len(image[0])
    
    # Change each RGB pixel value to the average of the three values.
    for row_index in range(num_rows):
        for column_index in range(num_columns):
            rgb = image[row_index][column_index]
            ave = (rgb[0] + rgb[1] + rgb[2]) / 3
            image[row_index][column_index] = [ave, ave, ave]

    return image

def flip_horizontal(image):
    """ This function mirrors the given image around a vertical line. """

    # Why is this operation needed?
    # The loop needs to run based on the original image, but the original image is modified while looping, so it needs a copy of the original one.

    image_copy = deepcopy(image)

    num_rows = len(image)
    num_columns = len(image[0])

    for row_index in range(num_rows):
        for column_index in range(num_columns):
            image[row_index][column_index] = image_copy[row_index][num_columns - column_index - 1]

    return image

def flip_vertical(image):
    '''This function mirrors the given image around a horizontal line.'''
    
    image_copy = deepcopy(image)

    num_rows = len(image)
    num_columns = len(image[0])

    for row_index in range(num_rows):
        for column_index in range(num_columns):
            image[row_index][column_index] = image_copy[num_rows - row_index - 1][column_index]

    return image

def snow(image):
    '''This function changes the image to random visual noises.'''
    
    import random
    
    num_rows = len(image)
    num_columns = len(image[0])
    
    # Set each RGB pixel value to a random number between 0 and 255.
    for row_index in range(num_rows):
        for column_index in range(num_columns):
            rgb = image[row_index][column_index]
            num = random.randint(0, 255)
            image[row_index][column_index] = [num, num, num]
            
    return image

def sepia(image):
    '''This function creates a sepia toning for the original image.'''
    
    num_rows = len(image)
    num_columns = len(image[0])
    
    # Reset each RGB pixel value using the color modifications suggested by Y. Garcia.
    for row_index in range(num_rows):
        for column_index in range(num_columns):
            rgb = image[row_index][column_index]
        
            red = (rgb[0] * .393) + (rgb[1] *.769) + (rgb[2] * .189)
            green = (rgb[0] * .349) + (rgb[1] *.686) + (rgb[2] * .168)
            blue = (rgb[0] * .272) + (rgb[1] *.534) + (rgb[2] * .131)
        
            image[row_index][column_index] = [red, green, blue]
    
    return image