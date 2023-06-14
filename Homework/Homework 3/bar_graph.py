"""CS 108 - Homework 3.0

This program draws a bar graph based on a list of user's inputs.

@author: ZeAi Sun (zs35)
@date: Fall, 2021
"""

# Import GuiZero and set up the canvas.
from guizero import App, Drawing
app = App('Bar Graph')
drawing = Drawing(app, width='fill', height='fill')


# Define a function to read integers from the user and return the integers as a list.
def get_data():

    data = []                                                     # Create an empty list to store integers.
    print('Please enter the data elements to graph.')

    while True:                                                   # Set up a while loop to keep getting data from the user until the user quits.
        num = int(input('integer (negative number to quit): '))       # Ask for an input from the user. Input a negative number to end the program.
        if num < 0:                                                   # Decide if the new input is positive or negative. If it's negative, step into quitting branches.
            if len(data) < 1:                                             # Decide if the user has inputted at least 1 number. If not, continue the loop.
                print('Please enter at least one number!')
                continue                                           
            else:                                                         # If the user has inputted at least 1 number, break the loop.
                break
        else:                                                         # If the new input is positive, store it into the empty list and continue the loop.
            data.append(num)

    return data                                                   # Return the list of integers.

# Define a function to randomly pick a color from a list of colors.
def get_random_color():
    import random
    return random.choice(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])

# Define a function to draw the bar graph based on a list of integers.
def draw_bar_graph(drawing, data, color='blue'):

#     data = get_data()                                             # Get a list of data through calling the get_data() function.
#     color = get_random_color()                                    # Get a random color through calling the get_random_color() function.
    unit_x = app.width / max(data)                                # Divide the canvas width by the larest value in data, set the result as the scale factor of x.
    unit_y = app.height / len(data)                               # Divide the canvas height by the number of values in data, set the result as the scale factor of y.

    for i in range(len(data)):                                    # Set up an index loop to go through all integers in the list.
        drawing.rectangle(                                            # Draw the appropriate bar based on the integer. 
            0, unit_y * i,                                                # x1 = 0, y1 = the y scale factor * the index of the bar
            unit_x * data[i], unit_y * (i + 1),                           # x2 = the x scale factor * the integer, y2 = the y scale factor * the index of the next bar
            color = color, outline = True                                 # Color is the output of the get_random_color() function.
            )

        # The guizero uses the coordinates of two points to draw the rectangle: the upper left point (x1, y1) and the lower right point (x2, y2).
        # For all bars, x1 is on the y axis, so it's always 0.
        # x2 is the length of the bar, calculated by multiplying the x scale factor to the integer value of the bar.
        # y1 is the sum of the width of all previous bars, calculated by multiplying the y scale factor to the index of the bar.
        # y2 - y1 = the width of the bar = the y scale factor, so y2 is calculated by multiplying the y scale factor to (the index of the bar + 1).

# Call the function to draw the bar graph.
draw_bar_graph(drawing, get_data(), get_random_color())

app.display()