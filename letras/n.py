import turtle


def letra_n(raphael: turtle.Turtle, init_x: int, init_y: int) -> None:
    raphael.penup()
    raphael.goto(init_x, init_y)
    pos_x = init_x - 225
    pos_y = init_y + 0
    raphael.pendown()
    raphael.goto(pos_x, pos_y)
    pos_x = init_x + 100
    raphael.goto(pos_x, pos_y)
