import turtle

raphael = turtle.Turtle()

def letra_o() -> None:
    raphael.penup()
    raphael.pensize(5)
    raphael.goto(25, 0)
    raphael.pendown()
    raphael.left(90)
    raphael.forward(100)
    raphael.right(90)
    raphael.forward(50)
    raphael.right(90)
    raphael.forward(100)
    raphael.right(90)
    raphael.forward(50)
    raphael.left(90)