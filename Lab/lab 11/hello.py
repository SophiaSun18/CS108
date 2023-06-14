"""CS 108 Lab 11.0

This module builds a GUI interfaces.

@author: Keith VanderLinden (kvlinden)
@date: Spring, 2021
@author: ZeAi Sun (zs35)
@date: Fall, 2021
"""

from guizero import App, Text, TextBox, PushButton


class MyApp:

    def __init__(self, app):

        # Configure the application GUI.
        app.title = 'My Application'
        app.width = 300
        app.height = 150
        app.font = 'Helvetica'
        app.text_size = 12

        # Add the widgets.
        hello_text = Text(app, text='Please enter your name:')
        user_name = TextBox(app)
        quit_bottom = PushButton(app, text='Goodbye!', command=app.destroy)


# Create the GuiZero application.
app = App()
my_app = MyApp(app)
app.display()
