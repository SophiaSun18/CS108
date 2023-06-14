import turtle as t

t.Screen()
t.setup(width = 1400, height = 1400)
pen = t.Pen()

unit = 180

t.colormode(255)

# Adjust the color for the red flag
pen.pencolor((238, 28, 37))
pen.fillcolor((238, 28, 37))

# Draw the red flag
pen.begin_fill()
pen.forward(unit * 3)
pen.right(90)
pen.forward(unit * 2)
pen.right(90)
pen.forward(unit * 3)
pen.right(90)
pen.forward(unit * 2)
pen.end_fill()
pen.up()

# Adjust the color for the yellow stars
pen.pencolor((255, 255, 0))
pen.fillcolor((255, 255, 0))

# Find the central point of the big yellow star
pen.up()
pen.right(90)
pen.forward(unit * 0.2)
pen.right(90)
pen.forward(unit * 0.4)
pen.left(90)

# Draw the big yellow star
pen.begin_fill()

pen.forward(unit * 0.6)
pen.right(144)
pen.forward(unit * 0.6)
pen.right(144)
pen.forward(unit * 0.6)
pen.right(144)
pen.forward(unit * 0.6)
pen.right(144)
pen.forward(unit * 0.6)

pen.end_fill()

# Find the central point of the 1st small yellow star
pen.up()
pen.right(144)
pen.forward(unit * 0.7)
pen.left(90)
pen.forward(unit * 0.2)
pen.right(90)
pen.down()

# Draw the 1st small yellow star
pen.begin_fill()

pen.forward(unit * 0.2)
pen.right(144)
pen.forward(unit * 0.2)
pen.right(144)
pen.forward(unit * 0.2)
pen.right(144)
pen.forward(unit * 0.2)
pen.right(144)
pen.forward(unit * 0.2)

pen.end_fill()

# Find the central point of the 2nd small yellow star
pen.up()
pen.right(144)
pen.forward(unit * 0.2)
pen.right(90)
pen.forward(unit * 0.2)
pen.left(90)
pen.down()

# Draw the 2nd small yellow star
pen.begin_fill()

pen.forward(unit * 0.2)
pen.right(144)
pen.forward(unit * 0.2)
pen.right(144)
pen.forward(unit * 0.2)
pen.right(144)
pen.forward(unit * 0.2)
pen.right(144)
pen.forward(unit * 0.2)

pen.end_fill()

# Find the central point of the 3rd small yellow star
pen.up()
pen.left(126)
pen.forward(unit * 0.2)
pen.left(90)
pen.down()

# Draw the 3rd small yellow star
pen.begin_fill()

pen.forward(unit * 0.2)
pen.right(144)
pen.forward(unit * 0.2)
pen.right(144)
pen.forward(unit * 0.2)
pen.right(144)
pen.forward(unit * 0.2)
pen.right(144)
pen.forward(unit * 0.2)

pen.end_fill()

# Find the central point of the 4th small yellow star
pen.up()
pen.left(126)
pen.forward(unit * 0.2)
pen.right(90)
pen.forward(unit * 0.2)
pen.left(180)
pen.down()


# Draw the 4th small yellow star
pen.begin_fill()

pen.forward(unit * 0.2)
pen.right(144)
pen.forward(unit * 0.2)
pen.right(144)
pen.forward(unit * 0.2)
pen.right(144)
pen.forward(unit * 0.2)
pen.right(144)
pen.forward(unit * 0.2)

pen.end_fill()

pen.hideturtle()