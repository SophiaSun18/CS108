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
@date: Spring, 2020 - ported from Java/Processing, Fall, 2010
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


def brighten(image):
    """ This function makes the given image brighter. """

    num_rows = len(image)
    num_columns = len(image[0])

    # Increase each RGB pixel value.
    for row_index in range(num_rows):
        for column_index in range(num_columns):
            rgb = image[row_index][column_index]
            image[row_index][column_index] = [
                rgb[0] + 25,
                rgb[1] + 25,
                rgb[2] + 25
            ]

    return image


def dim(image):
    """ This function makes the given image dimmer. """

    num_rows = len(image)
    num_columns = len(image[0])

    # Decrease each RGB pixel value.
    for row_index in range(num_rows):
        for column_index in range(num_columns):
            rgb = image[row_index][column_index]
            image[row_index][column_index] = [
                rgb[0] - 25,
                rgb[1] - 25,
                rgb[2] - 25
            ]

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
