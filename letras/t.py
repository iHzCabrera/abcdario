import turtle

raphael = turtle.Turtle()

def letra_t() -> None:
    raphael.penup()
    raphael.pensize(5)
    raphael.goto(-125, 100)
    raphael.pendown()
    raphael.right(0)
    raphael.forward(50)
    raphael.left(180)
    raphael.forward(25)
    raphael.left(90)
    raphael.forward(100)