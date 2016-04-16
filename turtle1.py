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


def draw_all_stars(turtle_, size=6):
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


def draw_square(turtle_, color, size=6, speed=100):
    turtle_.pencolor(color)
    turtle_.pendown()
    turtle_.fillcolor(color)
    turtle_.begin_fill()
    for i in range(4):
        turtle_.forward(size+75)
        turtle_.right(90)
    turtle_.end_fill()


def draw_rectangle(turtle_, color, size=4):
    turtle_.pencolor(color)
    turtle_.pendown()
    turtle_.fillcolor(color)
    turtle_.begin_fill()
    turtle_.forward(140)
    turtle_.right(90)
    turtle_.forward(20)
    turtle_.right(90)
    turtle_.forward(140)
    turtle_.right(90)
    turtle_.forward(20)
    turtle_.end_fill()
    pass


def main():
    turt = turtle.Turtle()
    turt.screen.bgcolor('white')
    turt.pencolor('white')

    # Position for blue square
    turt.left(90)
    turt.forward(90)
    turt.left(90)
    turt.forward(50)
    draw_square(turt, 'blue', 90)

    # Position for States' stars
    turt.forward(35)
    turt.right(90)
    turt.forward(30)
    turt.left(90)

    turt.pencolor('blue')
    draw_all_stars(turt, size=4)

    # Position for rectangles
    turt.right(180)
    turt.forward(157)
    turt.left(90)
    turt.forward(40)
    turt.right(90)

    draw_rectangle(turt, "red")
    turtle.done()


if __name__ == '__main__':
    main()
