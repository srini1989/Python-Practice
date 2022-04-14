import turtle

turtle = turtle.Turtle()

turtle.color("blue")
for i in range(9):
    turtle.forward(100)
    turtle.left(123)

turtle.color("red")
for i in range(9):
    turtle.forward(200)
    turtle.left(123)

turtle.done()
