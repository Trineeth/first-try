import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle()
sides = 6
length = 70
angle  = 360.0 / sides
for i in range(sides):
    polygon.forward(length)
    polygon.right(angle)


# turtle.done()

# turtle.Screen().bgcolor("Aqua")
# board = turtle.Turtle()
# board.forward(100)
# board.left(120)
# board.forward(100)
# board.left(120)
# board.forward(100)

# board.penup()
# board.right(150)
# board.forward(50)

# board.pendown()
# board.right(90)
# board.forward(100)

# board.right(120)
# board.forward(100)
# board.right(120)
# board.forward(100)
# turtle.done()
# wn = turtle.Screen()
# wn.bgcolor("light blue")
# wn.title("turtle")
# pen = turtle.Turtle()

# size = 0
# while   True:
#     for i in range(4):
#         pen.fd(size + 1)
#         pen.left(90)
#         size = size + 5
#     size = size + 1