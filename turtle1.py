import turtle


def draw_star(size, color, turtle_, speed_=100):
    angle = 120
    turtle_.speed(speed_)
    turtle_.fillcolor(color)
    turtle_.begin_fill()

    for side in range(5):
        turtle_.forward(size)
        turtle_.right(angle)
        turtle_.forward(size)
        turtle_.right(72 - angle)

    turtle_.end_fill()


def row_5(turtle_, size):
    for i in range(5):
        draw_star(size, "white", turtle_)
        turtle_.forward(20)

    turtle_.forward(8)
    turtle_.left(120)
    turtle_.forward(7)
    turtle_.left(60)
    turtle_.forward(15)


def row_6(turtle_, size):
    for i in range(6):
        draw_star(size, "white", turtle_)
        turtle_.forward(20)

    turtle_.right(120)
    turtle_.forward(20)
    turtle_.right(60)
    turtle_.forward(20)


def star_row(turtle_, size=6):
    row_6(turtle_, size)
    row_5(turtle_, size)
    row_6(turtle_, size)
    row_5(turtle_, size)
    row_6(turtle_, size)
    row_5(turtle_, size)
    row_6(turtle_, size)
    row_5(turtle_, size)

    for i in range(6):
        draw_star(size, "white", turtle_)
        turtle_.forward(20)


def main():
    turt = turtle.Turtle()
    turt.screen.bgcolor('blue')
    turt.pencolor('blue')
    star_row(turt, size=4)
    turtle.done()


if __name__ == '__main__':
    main()
